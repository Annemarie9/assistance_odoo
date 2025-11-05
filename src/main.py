import os
import sys
import json
import psycopg
from psycopg import Cursor
from openai import OpenAI
from dotenv import load_dotenv
from rag_system import RAGSYTEM
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Chatbot Assistance Odoo/GTHUB")
print(sys.executable)

# --- Charger les variables d'environnement ---
load_dotenv()

# --- Initialisation ---
data_path = "./data"
markdown_path = "./markdown_data"

openai_client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

db_connection_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={HOST} port={PORT}"

# --- Fonction pour enregistrer une conversation ---
def save_conversation(user_id, question, answer):
    """Sauvegarde la conversation dans la base de données"""
    try:
        with psycopg.connect(db_connection_str) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO chat_history (user_id, question, answer, created_at)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, question, answer, datetime.now()))
                conn.commit()
    except Exception as e:
        print(f"Erreur lors de l'enregistrement de la conversation : {e}")

# --- Initialisation du système RAG ---
rag_system = RAGSYTEM(
    openai_client=openai_client,
    db_connection_str=db_connection_str,
    data_path=data_path,
    markdown_path=markdown_path
)

# --- Interface Streamlit ---

st.image("src/images/gthup.png", width=120)
st.markdown("<h1 style='text-align:center;'>Bienvenue sur le chatbot intelligent assistant Odoo / GTHUB</h1>", unsafe_allow_html=True)

# --- Politique de confidentialité ---
@st.dialog("Politique de confidentialité")
def show_privacy_policy():
    st.write("""
    Vous êtes informé(e) que cette conversation peut être enregistrée, surveillée et conservée afin d'améliorer nos services. 
    Veuillez ne pas saisir de données privées, sensibles, personnelles ou réglementées. En utilisant ce chatbot, vous consentez à cette surveillance et à cet enregistrement. 
    Vous reconnaissez et acceptez également que les informations que vous fournissez et les réponses que vous recevez (collectivement, le « Contenu ») 
    puissent être utilisées pour améliorer, surveiller, maintenir et développer le chatbot et leurs offres respectives.
    """)
    if st.button("Fermer"):
        st.rerun()  # Ferme le popup

# Bouton pour ouvrir le popup
if st.button("Voir la politique de confidentialité"):
    show_privacy_policy()


# --- Gestion session ---
if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_id" not in st.session_state:
    # Génère un ID utilisateur temporaire unique (par exemple : "user_1234")
    st.session_state.user_id = f"user_{os.urandom(4).hex()}"

# --- Afficher l'historique ---
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# --- Détection du type de requête ---
def detect_query_type(user_query: str) -> str:
    keywords_markdown = [
        "installation", "guide", "tutoriel", "documentation", "odoo", "configurer", "utilisation",
        "module", "fonctionnalité", "explication", "comment", "readme", "doc", "setup"
    ]
    keywords_txt = ["gthub", "odoo_gthub"]

    if any(kw.lower() in user_query.lower() for kw in keywords_markdown):
        return "markdown"
    elif any(kw.lower() in user_query.lower() for kw in keywords_txt):
        return "txt"
    else:
        return "txt"

# --- Entrée utilisateur ---
if user_query := st.chat_input("Posez votre question ici..."):
    st.chat_message("user").write(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    query_type = detect_query_type(user_query)

    # --- Recherche et génération de la réponse ---
    with st.spinner("Analyse et génération de la réponse..."):
        try:
            if query_type == "txt":
                context = rag_system.semantic_search_markdown(user_query)
            else:
                context = rag_system.semantic_search(user_query)

            final_response = rag_system.generate_response(context, user_query)

        except Exception as e:
            final_response = f" Une erreur s'est produite : {str(e)}"

    # --- Afficher la réponse ---
    st.chat_message("assistant").write(final_response)
    st.session_state.messages.append({"role": "assistant", "content": final_response})

    # --- Enregistrer dans la base ---
    save_conversation(
        user_id=st.session_state.user_id,
        question=user_query,
        answer=final_response
    )

    # --- Sauvegarder localement ---
    with open("messages.json", "w", encoding="utf-8") as f:
        json.dump(st.session_state.messages, f, ensure_ascii=False, indent=2)

    # --- Sauvegarder dans la base de données ---
    with psycopg.connect(db_connection_str) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO chat_history (user_id, question, answer, created_at)
                VALUES (%s, %s, %s, %s)
            """, (st.session_state.user_id, user_query, final_response, datetime.now()))
            conn.commit()