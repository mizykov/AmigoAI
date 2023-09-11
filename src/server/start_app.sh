#!/usr/bin/env bash

APP_DIR=$(cd `dirname $0` && pwd)

python3 $APP_DIR/app.py \
    --tg_token "$TG_BOT_TOKEN" \
    --openai_api_key "$OPENAI_APY_KEY" \
    --postgres_host "$DB_HOST" \
    --postgres_port "$DB_PORT" \
    --postgres_name "$DB_NAME" \
    --postgres_user "$DB_USER" \
    --postgres_password "$DB_PASSWORD"
