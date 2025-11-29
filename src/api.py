from flask import Flask, request, jsonify
import psycopg
from dotenv import load_dotenv
import os
import hashlib
from datetime import datetime

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

# Configuration Base de données
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

# Vérification des variables
missing_vars = [k for k, v in {
    "DB_NAME": DB_NAME,
    "DB_USER": DB_USER,
    "DB_PASSWORD": DB_PASSWORD,
    "HOST": HOST,
    "PORT": PORT
}.items() if not v]

if missing_vars:
    print("❌ Variables manquantes :", missing_vars)

db_connection_str = (
    f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={HOST} port={PORT}"
)


def hash_password(password: str) -> str:
    """Hash le mot de passe avec SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

# ================== ENDPOINTS UTILISATEURS ==================

@app.route('/api/users', methods=['GET'])
def get_all_users():
    """Récupérer tous les utilisateurs"""
    try:
        with psycopg.connect(db_connection_str) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT id, prenom, nom, email, created_at
                    FROM users
                    ORDER BY created_at DESC
                """)
                users = cur.fetchall()

                users_list = [{
                    "id": u[0],
                    "prenom": u[1],
                    "nom": u[2],
                    "email": u[3],
                    "created_at": u[4].isoformat() if u[4] else None
                } for u in users]

        return jsonify({
            "success": True,
            "count": len(users_list),
            "users": users_list
        }), 200

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    """Récupérer un utilisateur par son ID"""
    try:
        with psycopg.connect(db_connection_str) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT id, prenom, nom, email, created_at
                    FROM users
                    WHERE id = %s
                """, (user_id,))
                user = cur.fetchone()

        if not user:
            return jsonify({"success": False, "error": "Utilisateur non trouvé"}), 404

        return jsonify({
            "success": True,
            "user": {
                "id": user[0],
                "prenom": user[1],
                "nom": user[2],
                "email": user[3],
                "created_at": user[4].isoformat() if user[4] else None
            }
        }), 200

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/users', methods=['POST'])
def create_user():
    """Créer un nouveau utilisateur"""
    try:
        data = request.get_json()

        # Validation des champs
        required_fields = ['prenom', 'nom', 'email', 'password']
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    "success": False,
                    "error": f"Le champ '{field}' est obligatoire"
                }), 400

        prenom, nom, email, password = data["prenom"], data["nom"], data["email"], data["password"]

        if '@' not in email:
            return jsonify({"success": False, "error": "Email invalide"}), 400

        if len(password) < 6:
            return jsonify({"success": False, "error": "Mot de passe trop court"}), 400

        with psycopg.connect(db_connection_str) as conn:
            with conn.cursor() as cur:
                # Vérifier email existant
                cur.execute("SELECT id FROM users WHERE email = %s", (email,))
                if cur.fetchone():
                    return jsonify({"success": False, "error": "Email déjà utilisé"}), 409

                hashed_pwd = hash_password(password)
                cur.execute("""
                    INSERT INTO users (prenom, nom, email, password, created_at)
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING id, prenom, nom, email, created_at
                """, (prenom, nom, email, hashed_pwd, datetime.now()))

                user = cur.fetchone()
                conn.commit()

        return jsonify({
            "success": True,
            "message": "Utilisateur créé",
            "user": {
                "id": user[0],
                "prenom": user[1],
                "nom": user[2],
                "email": user[3],
                "created_at": user[4].isoformat()
            }
        }), 201

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
# ================== ENDPOINTS CONVERSATIONS ==================

@app.route('/api/conversations', methods=['GET'])
def get_all_conversations():
    """Récupérer toutes les conversations"""
    try:
        with psycopg.connect(db_connection_str) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT ch.id, ch.user_id, u.prenom, u.nom, u.email,  
                           ch.question, ch.answer, ch.created_at
                    FROM chat_history ch
                    JOIN users u ON ch.user_id = u.id
                    ORDER BY ch.created_at DESC
                """)
                conversations = cur.fetchall()

                conv_list = []
                for conv in conversations:
                    conv_list.append({
                        "id": conv[0],
                        "user_id": conv[1],
                        "user": {
                            "prenom": conv[2],
                            "nom": conv[3],
                            "email": conv[4]
                        },
                        "question": conv[5],
                        "answer": conv[6],
                        "created_at": conv[7].isoformat() if conv[7] else None
                    })

                return jsonify({
                    "success": True,
                    "count": len(conv_list),
                    "conversations": conv_list
                }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/users/<int:user_id>/conversations', methods=['GET'])    
def get_user_conversations(user_id):
    """Récupérer les conversations d'un utilisateur spécifique"""        
    try:
        with psycopg.connect(db_connection_str) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT ch.id, ch.question, ch.answer, ch.created_at  
                    FROM chat_history ch
                    WHERE ch.user_id = %s
                    ORDER BY ch.created_at DESC
                """, (user_id,))
                conversations = cur.fetchall()

                conv_list = []
                for conv in conversations:
                    conv_list.append({
                        "id": conv[0],
                        "question": conv[1],
                        "answer": conv[2],
                        "created_at": conv[3].isoformat() if conv[3] else None
                    })

                return jsonify({
                    "success": True,
                    "user_id": user_id,
                    "count": len(conv_list),
                    "conversations": conv_list
                }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/users/email/<email>/conversations', methods=['GET'])    
def get_user_conversations_by_email(email):
    """Récupérer les conversations d'un utilisateur par email"""
    try:
        with psycopg.connect(db_connection_str) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT ch.id, ch.user_id, u.prenom, u.nom,
                           ch.question, ch.answer, ch.created_at
                    FROM chat_history ch
                    JOIN users u ON ch.user_id = u.id
                    WHERE u.email = %s
                    ORDER BY ch.created_at DESC
                """, (email,))
                conversations = cur.fetchall()

                conv_list = []
                for conv in conversations:
                    conv_list.append({
                        "id": conv[0],
                        "user_id": conv[1],
                        "user": {
                            "prenom": conv[2],
                            "nom": conv[3],
                            "email": email
                        },
                        "question": conv[4],
                        "answer": conv[5],
                        "created_at": conv[6].isoformat() if conv[6] else None
                    })

                return jsonify({
                    "success": True,
                    "email": email,
                    "count": len(conv_list),
                    "conversations": conv_list
                }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# ================== (les autres endpoints restent inchangés) ==================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint de test général — ne plante pas si DB DOWN"""
    return jsonify({
        "success": True,
        "message": "API is running",
        "timestamp": datetime.now().isoformat()
    }), 200


if __name__ == '__main__':
    print("API Flask démarre sur http://0.0.0.0:5000 ...")
    app.run(debug=True, host='0.0.0.0', port=5000)
