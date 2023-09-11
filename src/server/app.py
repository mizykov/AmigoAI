import os

from argparse import ArgumentParser
from utils import ExternalConfig, FRIEND_PROMPT

from bot import bot_factory


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('--tg_token')
    parser.add_argument('--openai_api_key')
    parser.add_argument('--postgres_host')
    parser.add_argument('--postgres_port')
    parser.add_argument('--postgres_name')
    parser.add_argument('--postgres_user')
    parser.add_argument('--postgres_password')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()

    bd_config = ExternalConfig(
        host=args.postgres_host,
        port=args.postgres_port,
        name=args.postgres_name,
        user=args.postgres_user,
        password=args.postgres_password
    )

    bot = bot_factory.create_bot(args.tg_token, args.openai_api_key, bd_config, FRIEND_PROMPT)
    bot.infinity_polling()


if __name__ == "__main__":
    main()
