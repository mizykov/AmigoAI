import telebot


from bot.bot_manager import BotManager


def create_bot(tg_bot_token, openai_api_key, bd_config, prompt):
    bot = telebot.TeleBot(tg_bot_token)
    bot.manager = BotManager(openai_api_key, bd_config, prompt)

    @bot.message_handler(commands=['start', 'hello'])
    def start_command(message):
        answer = bot.manager.start()
        bot.send_message(message.chat.id, answer)

    @bot.message_handler(commands=['statistics'])
    def get_statistics(message):
        statistics = bot.manager.get_statistics()
        bot.send_message(message.chat.id, statistics)

    @bot.message_handler()
    def gpt(message):
        answer = bot.manager.ask_gpt(message.text)
        bot.send_message(message.chat.id, answer)

    return bot
