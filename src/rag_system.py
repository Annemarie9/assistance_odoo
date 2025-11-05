import os
import psycopg
from psycopg import Cursor
from datetime import datetime


class RAGSYTEM:

    def __init__(self, openai_client: str, db_connection_str: str, data_path: str, markdown_path: str):
        self.openai_client = openai_client
        self.db_connection_str = db_connection_str
        self.data_path = data_path
        self.markdown_path = markdown_path

        # --- Initialisation de la base de données ---
        with psycopg.connect(db_connection_str) as conn:
            with conn.cursor() as cur:
                # Activer l'extension vector
                cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")

                # Table pour les fichiers .txt
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS embeddings (
                        id serial PRIMARY KEY,
                        document text,
                        embedding vector(1536)
                    );
                """)

                # Table pour les fichiers Markdown
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS markdown_embeddings (
                        id serial PRIMARY KEY,
                        filename text,
                        content text,
                        embedding vector(1536)
                    );
                """)

                # Table d'historique des conversations
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS chat_history (
                        id serial PRIMARY KEY,
                        user_id VARCHAR(100) NOT NULL,
                        question TEXT NOT NULL,
                        answer TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)
                conn.commit()

    # === Helper pour calculer les embeddings ===
    def compute_embedding(self, document: str) -> list[float]:
        if len(document) > 15000:
            document = document[:15000]

        embeddings = self.openai_client.embeddings.create(
            model="text-embedding-3-small",
            input=document,
            encoding_format="float"
        ).data
        return embeddings[0].embedding

    # === Enregistrement des embeddings TXT ===
    def save_embedding(self, document: str, embedding: list[float], cursor: Cursor) -> None:
        cursor.execute("""
            INSERT INTO embeddings (document, embedding)
            VALUES (%s, %s)
        """, (document, embedding))

    # === Enregistrement des embeddings Markdown ===
    def save_markdown_embedding(self, filename: str, content: str, embedding: list[float], cursor: Cursor) -> None:
        cursor.execute("""
            INSERT INTO markdown_embeddings (filename, content, embedding)
            VALUES (%s, %s, %s)
        """, (filename, content, embedding))

    # === Stockage des documents TXT ===
    def store_documents(self) -> None:
        with psycopg.connect(self.db_connection_str) as conn:
            with conn.cursor() as cur:
                documents_path = [f for f in os.listdir(self.data_path) if f.endswith('.txt')]

                for doc in documents_path:
                    file_path = os.path.join(self.data_path, doc)
                    with open(file_path, "r", encoding='utf-8', errors="replace") as file:
                        document = file.read()
                        embedding = self.compute_embedding(document)
                        self.save_embedding(document, embedding, cur)

                conn.commit()
                print(" Tous les documents TXT ont été enregistrés.")

    # === Stockage des fichiers Markdown ===
    def store_markdown_documents(self, chunk_size=5000) -> None:
        with psycopg.connect(self.db_connection_str) as conn:
            with conn.cursor() as cur:
                markdown_files = [f for f in os.listdir(self.markdown_path) if f.endswith('.md')]

                for md_file in markdown_files:
                    file_path = os.path.join(self.markdown_path, md_file)
                    with open(file_path, "r", encoding='utf-8', errors="replace") as file:
                        content = file.read()

                        chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]
                        for idx, chunk in enumerate(chunks):
                            try:
                                embedding = self.compute_embedding(chunk)
                                self.save_markdown_embedding(f"{md_file}_part{idx + 1}", chunk, embedding, cur)
                            except Exception as e:
                                print(f" Erreur lors de l'enregistrement du chunk {idx + 1} de {md_file} : {e}")

                conn.commit()
                print(" Tous les fichiers Markdown ont été enregistrés.")

    # === Vérifie si des embeddings Markdown existent déjà ===
    def has_embeddings_markdown(self) -> bool:
        with psycopg.connect(self.db_connection_str) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM markdown_embeddings;")
                count = cur.fetchone()[0]
                return count > 0

    # === Vérifie si des embeddings TXT existent déjà ===
    def has_embeddings_txt(self) -> bool:
        with psycopg.connect(self.db_connection_str) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM embeddings;")
                count = cur.fetchone()[0]
                return count > 0

    # === Recherche sémantique pour fichiers TXT ===
    def semantic_search(self, user_query: str) -> str:
        user_query_embedding = self.compute_embedding(user_query)
        with psycopg.connect(self.db_connection_str) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT document
                    FROM embeddings
                    ORDER BY embedding <=> %s::vector ASC
                    LIMIT 1;
                """, [user_query_embedding])
                result = cur.fetchone()
                return result[0] if result else "Aucun résultat trouvé."

    # === Recherche sémantique pour fichiers Markdown ===
    def semantic_search_markdown(self, user_query: str) -> str:
        user_query_embedding = self.compute_embedding(user_query)
        with psycopg.connect(self.db_connection_str) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT filename, content
                    FROM markdown_embeddings
                    ORDER BY embedding <=> %s::vector ASC
                    LIMIT 1;
                """, [user_query_embedding])
                result = cur.fetchone()
                if result:
                    filename, content = result
                    return f" **{filename}**\n\n{content}"
                return "Aucun fichier Markdown correspondant trouvé."

    # === Génération de la réponse finale ===
    def generate_response(self, context: str, user_query: str):
        MAX_CONTEXT_LENGTH = 100000
        if len(context) > MAX_CONTEXT_LENGTH:
            context = context[:MAX_CONTEXT_LENGTH]

        completion = self.openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"Tu es un assistant de la documentation Odoo et locale. "
                        f"Réponds à la question suivante : {user_query}, "
                        f"en utilisant ces informations : {context}"
                    ),
                }
            ],
        )
        return completion.choices[0].message.content
