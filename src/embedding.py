# embed_markdown.py
import os
from dotenv import load_dotenv
from openai import OpenAI
from rag_system import RAGSYTEM

# Charger les variables d'environnement
load_dotenv()

# Configurations
data_path = "./data"
markdown_path = "./markdown_data"

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
OPENAI_KEY = os.getenv("OPENAI_KEY")

# Initialiser les clients
openai_client = OpenAI(api_key=OPENAI_KEY)
db_connection_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={HOST} port={PORT}"

# Initialiser ton système RAG
rag_system = RAGSYTEM(
    openai_client=openai_client,
    db_connection_str=db_connection_str,
    data_path=data_path,
    markdown_path=markdown_path
)

# --- Exécuter l’embedding une seule fois ---
print(" Création des embeddings à partir des fichiers Markdown...")
if not rag_system.has_embeddings_markdown():
    print(" Embeddings Markdown non trouvés, création des embeddings...")
    rag_system.store_markdown_documents()
else:
    print(" Embeddings enregistrés avec succès dans la base PostgreSQL.")
print(" Création des embeddings à partir des fichiers txt...")
if not rag_system.has_embeddings_txt():
    print(" Embeddings TXT non trouvés, création des embeddings...")
    rag_system.store_documents()
else:    
    print("Embeddings enregistrés avec succès dans la base PostgreSQL.")
