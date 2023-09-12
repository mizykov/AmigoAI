FROM python:3.8-slim-buster

WORKDIR /

RUN pip install torch==1.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html --no-cache-dir
RUN pip install --no-deps sentence-similarity
RUN pip install --no-deps sentence-transformers

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY src/ src/
COPY src/server/start_app.sh src/server/start_app.sh
RUN chmod 777 src/server/start_app.sh

CMD src/server/start_app.sh
