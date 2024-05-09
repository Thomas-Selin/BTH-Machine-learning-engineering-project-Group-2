FROM amd64/python:latest

# Create app directory
WORKDIR /app
# Copy the files
COPY requirements.txt ./
COPY app.py ./
COPY rag_engine.py ./
COPY documents/ ./documents/

#install the dependecies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir spacy

EXPOSE 7860
ENTRYPOINT [ "python", "-u", "app.py" ]
