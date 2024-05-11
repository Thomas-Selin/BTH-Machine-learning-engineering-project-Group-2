FROM --platform=linux/amd64 amd64/python:latest

WORKDIR /app

COPY requirements.txt ./
COPY app.py ./
COPY rag_engine.py ./
COPY documents/ ./documents/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir spacy

EXPOSE 7860
ENTRYPOINT [ "python", "-u", "app.py" ]
