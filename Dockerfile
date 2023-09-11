FROM python:3.8-slim-buster

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY src/ src/
COPY src/server/start_app.sh src/server/start_app.sh
RUN chmod 777 src/server/start_app.sh

CMD src/server/start_app.sh
