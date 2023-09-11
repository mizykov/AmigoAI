import logging

import openai
import psycopg2


OPENAI_COMPLETION_OPTIONS = {
    "temperature": 0.7,
    "max_tokens": 1000,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "request_timeout": 60.0,
}

logging.basicConfig(
    filename='my_logs.txt',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG
)


class BotManager():

    def __init__(self, openai_api_key, bd_config, prompt):
        openai.api_key = openai_api_key
        self.bd_config = bd_config
        self.conn = psycopg2.connect(
            host=bd_config.host, 
            port=bd_config.port,
            dbname=bd_config.name,
            user=bd_config.user,
            password=bd_config.password
        )
        self.n_rows = 1
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO chat_history (message_id, role, text) VALUES (0, 'system', '{prompt}')")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def start(self, message):
        return "Hello! I am your new AI Friend, let's start our communication!"

    def ask_gpt(self, message):
        cur = self.conn.cursor()

        cur.execute("INSERT INTO chat_history VALUES (%s, %s, %s)", (self.n_rows, 'user', message))
        self.conn.commit()
        self.n_rows += 1

        cur.execute("SELECT * FROM chat_history;")
        rows = cur.fetchall()
        messages = []
        for row in rows:
            messages.append(
                {
                    "role": row[1],
                    "content": row[2]
                }
            )
        logging.info(f"\n mymessages: {messages}\n")

        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            **OPENAI_COMPLETION_OPTIONS
        )
        answer = response['choices'][0]['message']['content']

        cur = self.conn.cursor()
        cur.execute("INSERT INTO chat_history VALUES (%s, %s, %s)", (self.n_rows, 'assistant', answer))
        self.conn.commit()
        self.n_rows += 1

        return answer
