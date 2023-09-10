import telebot


def create_bot(token, bd_config):
    bot = telebot.TeleBot(token)
    # bot.manager = BotManager(bd_config)

    @bot.message_handler(commands=['start', 'hello'])
    def start_command(message):
        # answer = bot.manager.hello(message.from_user, message.text)
        answer = "What's up!"
        bot.send_message(message.chat.id, answer)

    return bot
