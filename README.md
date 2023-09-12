# AmigoAI Telegram Bot

<div align="center">
<img src="https://github.com/mizykov/AmigoAI/blob/dev/static/header_amigoai.png" align="center" style="width: 100%" />
</div>

<br>


## Welcome to my space, Amigo!

This project is a simple and hastily made realization of smart and emotional telegram bot. However, in the near future (literally a couple of weeks), this bot will improve to a decent level in order to benefit people.

## Features
- 🧑‍💻 **Interactive via telegram bot** The bot is waiting for you right in app Telegram
- 🧡 **Relationship development** Increase the level of trust and emotionality as you communicate
- 📚 **Knowledge base** The chatgpt from openal is taken as a basis, therefore all abilities also work here
- 👥 **Dialog context** The context of your dialog is saved and the bot keeps track of the history


## How to use it

Find the bot in Telegram and start a dialogue, the commands below will help you

### Bot commands
- `/hello or /start` – Start a dialog
- `/statistics` – Show dialog quality statistics


## How to deploy it

**Pre requirements**

- Docker
- Own Telegram bot
- The balance on openai for API

**Manual**

1. Make a copy of `example_env.txt` and rename to `.env`
2. Write your tokens of telegram bot and chatgpt API
3. Execute 'docker compose up' and your bot is ready
