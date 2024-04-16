FROM python:latest

ENV CURL_CA_BUNDLE=/usr/local/share/ca-certificates/ca.crt
ADD ca.crt /usr/local/share/ca-certificates/ca.crt
RUN chmod 644 /usr/local/share/ca-certificates/ca.crt
COPY ca.crt /etc/ssl/certs/
RUN update-ca-certificates

# Create app directory
WORKDIR /app

# Copy the files
COPY requirements.txt ./
COPY app.py ./
COPY rag_engine.py ./
COPY documents/ ./documents/
# COPY data/ ./data/

#install the dependecies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 7860
ENTRYPOINT [ "python", "-u", "app.py" ]
# ENTRYPOINT [ "bash" ]
