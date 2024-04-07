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

1. Clone this repo: ```git clone git@github.com:ttechstuff/group2-ML-app-v1.git; cd group2-ML-app-v1```

2. Download and start [Docker Desktop](https://www.docker.com/products/docker-desktop/).

3. Build the application image.

```
docker build . -t application
```

4. Start the servers.

```
docker-compose up --detach
```

5. Download and set up a model of your choice (that your hardware can handle). In this example the model is named **phi**. You can find other models [here](https://ollama.com/library).

```
docker exec model-container ollama run phi
```

## How to use the chatbot  <span id="HowToUse"><span>

You can find the chatbot here: [http://localhost:8501](http://localhost:8501)

## How to develop

To make changes to the code and start the servers with the new changes applied:
1. ```docker compose down```
2. Check out a feature branch: ```git checkout -b <what you want to call your branch>```
3. Make your code changes
4. ```docker build . -t application```
5. ```docker-compose up --detach```
6. See [How to use](#HowToUse)
7. If you are happy with your changes and want to share to the group, commit and push: ```git commit -am "<description of you code changes>"; git push --set-upstream origin <what you called your branch>```
8. When pushing further code you can omit ```--set-upstream origin <what you called your branch>``` from the command above

## Various non-essential information
For various experimentation you can communicate directly with the Ollama API via [http://localhost:11434](http://localhost:11434) in the way described here: [Ollama API documentation](https://github.com/ollama/ollama/blob/main/docs/api.md)

For more info about the server setup, see docker-compose.yml file.
