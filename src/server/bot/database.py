import psycopg2


class BotDatabase:
    def __init__(self, bd_config):
        self.conn = psycopg2.connect(
            host=bd_config.host, 
            port=bd_config.port,
            dbname=bd_config.name,
            user=bd_config.user,
            password=bd_config.password
        )

    def insert_to_messages(self, message_id, role, text):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO chat_history VALUES (%s, %s, %s)", (message_id, role, text))
        self.conn.commit()

    def insert_to_scores(self, score_id, answer_id, score):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO scores_history VALUES (%s, %s, %s)", (score_id, answer_id, score))
        self.conn.commit()

    def get_rows(self, table_name):
        cur = self.conn.cursor()
        if table_name == 'chat_history':
            cur.execute("SELECT * FROM chat_history;")
        else:
            cur.execute("SELECT * FROM scores_history;")
        rows = cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()
