FROM python:latest

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

EXPOSE 7860
ENTRYPOINT [ "python", "-u", "app.py" ]
