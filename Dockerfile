FROM python:3.8-slim-buster

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY src/ src/
COPY tools/start_bot.sh tools/start_bot.sh

CMD tools/start_bot.sh
