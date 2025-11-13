import os
import sys
import json
import psycopg
from openai import OpenAI
from dotenv import load_dotenv
from rag_system import RAGSYTEM
import streamlit as st
from datetime import datetime
from  token_manager import TokenManager
# --- Configuration Streamlit ---
st.set_page_config(page_title="Chatbot Assistance Odoo / GTHUB")
print(sys.executable)

# --- Charger les variables d'environnement ---
load_dotenv()

# --- Initialisation OpenAI ---
openai_client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

# --- Configuration Base de données ---
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

db_connection_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={HOST} port={PORT}"

# --- Initialisation du système RAG ---
rag_system = RAGSYTEM(
    openai_client=openai_client,
    db_connection_str=db_connection_str,
    data_path="./data",
    markdown_path="./markdown_data"
)
token_manager = TokenManager(db_connection_str)


# --- Logo et titre ---
st.image("src/images/gthup.png", width=120)
st.markdown("<h1 style='text-align:center;'>Bienvenue sur le Chatbot Intelligent Odoo / GTHUB</h1>", unsafe_allow_html=True)

# --- Politique de confidentialité ---
@st.dialog("Politique de confidentialité")
def show_privacy_policy():
    st.write("""
    Vous êtes informé(e) que cette conversation peut être enregistrée, surveillée et conservée afin d'améliorer nos services. 
    Veuillez ne pas saisir de données privées, sensibles, personnelles ou réglementées. En utilisant ce chatbot, vous consentez à cette surveillance et à cet enregistrement. 
    """)
    if st.button("Fermer"):
        st.rerun()

if st.button("Voir la politique de confidentialité"):
    show_privacy_policy()

# --- Étape 1 : Connexion utilisateur ---
if "email" not in st.session_state:
    st.markdown("###  Connexion utilisateur")
    email = st.text_input("Entrez votre adresse e-mail pour continuer :")

    if st.button("Se connecter"):
        if not email or "@" not in email:
            st.error("Veuillez saisir une adresse e-mail valide.")
        else:
            user_id = rag_system.get_or_create_user(email)
            st.session_state.email = email
            st.session_state.user_id = user_id
            st.success(f"Bienvenue {email} !")
            st.rerun()
    st.stop()

# --- Étape 2 : Charger ou initialiser les messages ---
if "messages" not in st.session_state:


    st.session_state.messages = []

   
# --- Afficher l'historique de la session ---
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# --- Fonctions utilitaires ---
def detect_query_type(user_query: str) -> str:
    keywords_markdown = [
        "installation", "guide", "tutoriel", "documentation", "odoo", "configurer",
        "utilisation", "module", "fonctionnalité", "explication", "comment", "readme",
        "doc", "setup"
    ]
    keywords_txt = ["gthub", "odoo_gthub"]

    if any(kw.lower() in user_query.lower() for kw in keywords_markdown):
        return "markdown"
    elif any(kw.lower() in user_query.lower() for kw in keywords_txt):
        return "txt"
    else:
        return "txt"


def is_technical_question(query: str) -> bool:
    technical_keywords = [
        "erreur", "error", "bug", "crash", "problème", "failed",
        "installation", "installer", "configurer", "configuration",
        "dépendance", "serveur", "port", "connexion", "database",
        "authentification", "setup", "code", "debug"
    ]
    return any(word.lower() in query.lower() for word in technical_keywords)


def is_relevant_question(query: str) -> bool:
    relevant_keywords = [
        "odoo", "module", "facture", "vente", "crm", "stock", "gthub",
        "base de données", "serveur odoo", "interface odoo", "paramétrage",
        "installation odoo", "configuration odoo"
    ]
    return any(word.lower() in query.lower() for word in relevant_keywords)


# --- Étape 3 : Chat ---
if user_query := st.chat_input("Posez votre question ici..."):
    st.chat_message("user").write(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    # Vérifier si l'utilisateur a atteint sa limite
    if token_manager.has_reached_limit(st.session_state.user_id):
        st.warning("Vous avez atteint votre limite mensuelle de 2000 tokens.")
        st.stop()

    # Vérification de pertinence
    if not is_relevant_question(user_query):
        final_response = (
            "Désolé, je ne peux répondre qu’aux questions liées à **Odoo** ou **GTHUB**.\n\n"
            "Merci de reformuler votre question dans ce contexte."
        )
    else:
        query_type = detect_query_type(user_query)

        if query_type == "txt" and is_technical_question(user_query):
            final_response = (
                "Cette question semble concerner une **configuration** ou un **problème technique**.\n\n"
                "Merci de contacter notre **support technique** pour obtenir une assistance personnalisée."
            )
        else:
            with st.spinner("Analyse et génération de la réponse..."):
                try:
                    if query_type == "txt":
                        context = rag_system.semantic_search_markdown(user_query)
                    else:
                        context = rag_system.semantic_search(user_query)

                    final_response , usage = rag_system.generate_response_with_usage(context, user_query)
                    tokens_used = usage.prompt_tokens + usage.completion_tokens
                    token_manager.update_user_tokens(st.session_state.user_id, tokens_used)
                except Exception as e:
                    final_response = f"Une erreur s'est produite : {str(e)}"





    # --- Affichage et enregistrement ---
    st.chat_message("assistant").write(final_response)
    st.session_state.messages.append({"role": "assistant", "content": final_response})

    rag_system.save_conversation(
        user_id=st.session_state.user_id,
        question=user_query,
        answer=final_response
    )

    # Sauvegarde locale JSON
    with open("messages.json", "w", encoding="utf-8") as f:
        json.dump(st.session_state.messages, f, ensure_ascii=False, indent=2)
