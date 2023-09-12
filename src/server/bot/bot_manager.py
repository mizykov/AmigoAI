import openai
import psycopg2

from bot.database import BotDatabase
from bot.evaluation import Scorer


OPENAI_COMPLETION_OPTIONS = {
    "temperature": 0.7,
    "max_tokens": 500,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "request_timeout": 60.0,
}


class BotManager():

    def __init__(self, openai_api_key, bd_config, prompt):
        openai.api_key = openai_api_key
        self.scorer = Scorer()
        self.db = BotDatabase(bd_config)
        self.n_rows = 1
        self.n_answers = 0
        self.db.insert_to_messages(
            message_id=0,
            role='system',
            text=prompt
        )

    def start(self):
        return "Hello! I am your new AI Friend, let's start our communication!"

    def get_statistics(self):
        rows = self.db.get_rows('scores_history')
        n_rows = len(rows)
        total_score = 0

        messages = []
        for row in rows:
            total_score += row[2]

        # TODO: check the empty of rows
        return f'Average quality of dialog: {(total_score / n_rows):.3f}; The quality of last answer: {rows[n_rows-1][2]}'

    def ask_gpt(self, message):
        self.db.insert_to_messages(
            message_id=self.n_rows,
            role='user',
            text=message
        )
        self.n_rows += 1

        rows = self.db.get_rows('chat_history')
        messages = []
        for row in rows:
            messages.append(
                {
                    "role": row[1],
                    "content": row[2]
                }
            )

        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            **OPENAI_COMPLETION_OPTIONS
        )
        answer = response['choices'][0]['message']['content']

        self.db.insert_to_messages(
            message_id=self.n_rows,
            role='assistant',
            text=answer
        )
        self.n_rows += 1

        similarity_score = self.scorer.messure_score(message, answer)

        self.db.insert_to_scores(
            score_id=self.n_answers,
            answer_id=self.n_rows - 1,
            score=similarity_score
        )
        self.n_answers += 1

        return answer
