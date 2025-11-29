import os
import psycopg
from psycopg import Cursor
from datetime import datetime
from token_manager import TokenManager


class RAGSYTEM:

    def __init__(self, openai_client: str, db_connection_str: str, data_path: str, markdown_path: str):
        self.openai_client = openai_client
        self.db_connection_str = db_connection_str
        self.data_path = data_path
        self.markdown_path = markdown_path

        # --- Initialisation des tables (création si absentes uniquement) ---
        with psycopg.connect(db_connection_str) as conn:
            with conn.cursor() as cur:
                # Activer l'extension vector
                cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")

                # Tables principales
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        email TEXT UNIQUE NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)

                cur.execute("""
                    CREATE TABLE IF NOT EXISTS embeddings (
                        id serial PRIMARY KEY,
                        document text,
                        embedding vector(1536)
                    );
                """)

                cur.execute("""
                    CREATE TABLE IF NOT EXISTS markdown_embeddings (
                        id serial PRIMARY KEY,
                        filename text,
                        content text,
                        embedding vector(1536)
                    );
                """)

                cur.execute("""
                    CREATE TABLE IF NOT EXISTS chat_history (
                        id serial PRIMARY KEY,
                        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                        question TEXT NOT NULL,
                        answer TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)

                cur.execute("""
                    CREATE TABLE IF NOT EXISTS user_tokens (
                        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                        tokens_used INTEGER DEFAULT 0,
                        month_start DATE DEFAULT CURRENT_DATE,
                        PRIMARY KEY (user_id)
                    );
                """)

                conn.commit()

    # === Gestion des utilisateurs ===
    def get_or_create_user(self, email: str) -> int:
        with psycopg.connect(self.db_connection_str) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id FROM users WHERE email = %s;", (email,))
                user = cur.fetchone()
                if user:
                    return user[0]

                cur.execute("INSERT INTO users (email) VALUES (%s) RETURNING id;", (email,))
                user_id = cur.fetchone()[0]
                conn.commit()
                return user_id

    def get_user_history(self, user_id: int):
        with psycopg.connect(self.db_connection_str) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT question, answer, created_at
                    FROM chat_history
                    WHERE user_id = %s
                    ORDER BY created_at ASC;
                """, (user_id,))
                return cur.fetchall()

    def save_conversation(self, user_id: int, question: str, answer: str):
        with psycopg.connect(self.db_connection_str) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO chat_history (user_id, question, answer, created_at)
                    VALUES (%s, %s, %s, %s);
                """, (user_id, question, answer, datetime.now()))
                conn.commit()

    # === Embeddings ===
    def compute_embedding(self, document: str) -> list[float]:
        if len(document) > 15000:
            document = document[:15000]

        embeddings = self.openai_client.embeddings.create(
            model="text-embedding-3-small",
            input=document,
            encoding_format="float"
        ).data
        return embeddings[0].embedding

    def save_embedding(self, document: str, embedding: list[float], cursor: Cursor) -> None:
        cursor.execute("""
            INSERT INTO embeddings (document, embedding)
            VALUES (%s, %s)
        """, (document, embedding))

    def save_markdown_embedding(self, filename: str, content: str, embedding: list[float], cursor: Cursor) -> None:
        cursor.execute("""
            INSERT INTO markdown_embeddings (filename, content, embedding)
            VALUES (%s, %s, %s)
        """, (filename, content, embedding))

    def store_documents(self) -> None:
        """Stocke les fichiers TXT uniquement si la table embeddings est vide"""
        with psycopg.connect(self.db_connection_str) as conn:
            with conn.cursor() as cur:
                # Vérifie si des embeddings existent déjà
                cur.execute("SELECT COUNT(*) FROM embeddings;")
                count = cur.fetchone()[0]
                if count > 0:
                    print(" Les embeddings TXT existent déjà. Aucun recalcul nécessaire.")
                    return

                # Si vide, calcul et enregistrement
                documents_path = [f for f in os.listdir(self.data_path) if f.endswith('.txt')]
                for doc in documents_path:
                    file_path = os.path.join(self.data_path, doc)
                    with open(file_path, "r", encoding='utf-8', errors="replace") as file:
                        document = file.read()
                        embedding = self.compute_embedding(document)
                        self.save_embedding(document, embedding, cur)

                conn.commit()
                print(" Tous les documents TXT ont été enregistrés.")

    def store_markdown_documents(self, chunk_size=5000) -> None:
        """Stocke les fichiers Markdown uniquement si la table est vide"""
        with psycopg.connect(self.db_connection_str) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM markdown_embeddings;")
                count = cur.fetchone()[0]
                if count > 0:
                    print(" Les embeddings Markdown existent déjà. Aucun recalcul nécessaire.")
                    return

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
                                print(f"Erreur lors de l'enregistrement du chunk {idx + 1} de {md_file} : {e}")

                conn.commit()
                print(" Tous les fichiers Markdown ont été enregistrés.")

    # === Recherche sémantique ===
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
                    return f"**{filename}**\n\n{content}"
                return "Aucun fichier Markdown correspondant trouvé."

    # === Génération de réponse et suivi de tokens ===
    def generate_response_with_usage(self, context: str, user_query: str):
        MAX_CONTEXT_LENGTH = 100000
        if len(context) > MAX_CONTEXT_LENGTH:
            context = context[:MAX_CONTEXT_LENGTH]

        completion = self.openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Tu es un assistant spécialisé dans Odoo et GTHUB. "
                        "Réponds de manière claire, concise et utile aux utilisateurs."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Question : {user_query}\n\n"
                        f"Contexte pertinent : {context}"
                    ),
                },
            ],
            max_tokens=500,
        )

        response_text = completion.choices[0].message.content
        usage = completion.usage  # contient total_tokens, prompt_tokens, completion_tokens

        return response_text, usage
