# Test-APP - Group 2 ML @ BTH 

This project has 3 parts:
1. A container that serves the ML model. The container is created automatically from the publicly available ```ollama/ollama``` image.
2. ```app.py```: Code for an streamlit application that provides a chatbot frontend for chatting with the ML model. This application is served in a separate container.
3. ```rag-engine.py```: This code is a potential start for implementing RAG using the pdf documents in the ```documents``` folder. This code is as of now NOT used by the application, but can be tested by running the following commands outside of Docker:

    ```
    # You need python version 3 installed (preferably version 3.12.2)
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    python rag-engine.py
    ```


## How to start

1. Download and start [Docker Desktop](https://www.docker.com/products/docker-desktop/).

2. Build the application image.

```
docker build . -t application
```

3. Start the servers.

```
docker-compose up --detach
```

4. Download and set up a model of your choice (that your hardware can handle). In this example the model is named "phi". You can find other models [here](https://ollama.com/library).

```
docker exec -it model-container ollama run phi
```

## How to use

You can find the chatbot here: [http://localhost:8501](http://localhost:8501)

## How to develop

To make changes to the code and start the servers with the new changes applied:
1. ```docker compose down```
2. Make your code changes
3. ```docker build . -t application```
4. ```docker-compose up --detach```

## Various non essential information
For various experimentation you can communicate directly with the Ollama API via [http://localhost:11434](http://localhost:11434) in the way described here: [Ollama API documentation](https://github.com/ollama/ollama/blob/main/docs/api.md)

For more info about the server setup, see docker-compose.yml file.
