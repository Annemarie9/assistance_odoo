# token_manager.py
import psycopg
from datetime import date, timedelta

MAX_TOKENS_PER_MONTH = 50000

class TokenManager:
    def __init__(self, db_connection_str):
        self.db_connection_str = db_connection_str

    def get_user_tokens(self, user_id):
        """Récupère les infos token d’un utilisateur"""
        with psycopg.connect(self.db_connection_str) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT tokens_used, month_start
                    FROM user_tokens
                    WHERE user_id = %s
                """, (user_id,))
                result = cur.fetchone()

                if result:
                    tokens_used, month_start = result
                    # Si on est dans un nouveau mois → reset
                    if date.today() - month_start >= timedelta(days=30):
                        cur.execute("""
                            UPDATE user_tokens
                            SET tokens_used = 0, month_start = %s
                            WHERE user_id = %s
                        """, (date.today(), user_id))
                        conn.commit()
                        return 0
                    return tokens_used
                else:
                    # Crée un nouvel utilisateur
                    cur.execute("""
                        INSERT INTO user_tokens (user_id, tokens_used, month_start)
                        VALUES (%s, 0, %s)
                    """, (user_id, date.today()))
                    conn.commit()
                    return 0

    def update_user_tokens(self, user_id, tokens_used):
        """Met à jour le total de tokens utilisés"""
        with psycopg.connect(self.db_connection_str) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE user_tokens
                    SET tokens_used = tokens_used + %s
                    WHERE user_id = %s
                """, (tokens_used, user_id))
                conn.commit()

    def has_reached_limit(self, user_id):
        """Vérifie si l’utilisateur a dépassé son quota"""
        tokens_used = self.get_user_tokens(user_id)
        return tokens_used >= MAX_TOKENS_PER_MONTH
