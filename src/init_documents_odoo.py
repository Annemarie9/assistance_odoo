import os
import psycopg2


# Répertoire des fichiers
BASE_DIR = "raw_data/versions"

# Configuration OpenAI (tu peux la commenter si tu ne veux pas encore générer d'embeddings)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "sk-xxx"))

# Connexion PostgreSQL
conn = psycopg2.connect(
    HOST="postgres",
    port=5432,
    DB_NAME="chatbot_db",
    DB_USER="postgres",
    DB_PASSWORD="chatbot123"
)
cur = conn.cursor()

# Création de la table si elle n’existe pas encore
cur.execute("""
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS documents (
    id SERIAL PRIMARY KEY,
    path TEXT UNIQUE NOT NULL,
    content TEXT,
    embedding vector(1536)
);
""")
conn.commit()


def read_file_content(file_path: str) -> str | None:
    """Lit le contenu d’un fichier texte."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f" Erreur lecture {file_path}: {e}")
        return None


def generate_embedding(text: str) -> list[float]:
    """Génère un embedding de 1536 dimensions via OpenAI."""
    try:
        response = client.embeddings.create(
            model="text-embedding-ada-002",
            input=text
        )
        return response.data[0].embedding
    except Exception as e:
        print(f" Erreur embedding : {e}")
        return [0.0] * 1536  # vecteur vide par défaut


# Parcours récursif des fichiers
for root, _, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith((".rst", ".md", ".txt")):
            path = os.path.join(root, file)
            content = read_file_content(path)

            if content:
                embedding = generate_embedding(content[:2000])  # limiter le texte pour éviter les coûts élevés

                cur.execute("""
                    INSERT INTO documents (path, content, embedding)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (path) DO NOTHING;
                """, (path, content, embedding))
                print(f" Ajouté : {path}")

conn.commit()
cur.close()
conn.close()

print("Base de données initialisée avec succès.")
