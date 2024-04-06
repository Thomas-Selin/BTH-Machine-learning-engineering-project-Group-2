FROM python:latest

ENV CURL_CA_BUNDLE=/usr/local/share/ca-certificates/sbab-ca.crt
ADD ca.crt /usr/local/share/ca-certificates/sbab-ca.crt
RUN chmod 644 /usr/local/share/ca-certificates/sbab-ca.crt
COPY ca.crt /etc/ssl/certs/
COPY ca.crt /etc/docker/certs.d/ollama.ai
COPY ca.crt /etc/docker/certs.d/registry.ollama.ai
ADD ca.crt /usr/local/share/ca-certificates/my-ca.crt
RUN update-ca-certificates

# Create app directory
WORKDIR /app

# Copy the files
COPY requirements.txt ./
COPY app.py ./

#install the dependecies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py", "--global.logLevel=debug", "--server.port=8501", "--server.address=0.0.0.0"]
