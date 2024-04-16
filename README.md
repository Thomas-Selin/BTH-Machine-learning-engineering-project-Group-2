# Test-APP - Group 2 ML @ BTH 

This project has 3 parts:
1. A container that serves the ML model. The container is created automatically from the publicly available ```ghcr.io/huggingface/text-generation-inference:1.4``` image.
2. ```app.py```: Code for an gradio application that provides a chatbot frontend for chatting with the ML model. This application is served in a separate container.
3. ```rag-engine.py```: This code is implementing RAG by searching in the ```documents``` folder for the document that most relates to the users quesiton.

## How to start

1. Clone this repo: ```git clone git@github.com:ttechstuff/group2-ML-app-v1.git; cd group2-ML-app-v1```

2. Download, install, and start [Docker Desktop](https://www.docker.com/products/docker-desktop/).

3. Build the application image.

```
docker build . -t application
```

4. Provide a huggingface-token (HUGGINGFACE_TOKEN) in the docker-compose.yml file to simplify the initial download of the model. This requires a free huggingface account and an accesstoken with read permission.

5. Start the servers.

```
docker-compose up --detach
```

This downloads and sets up the model named **bigscience/mt0-small** (several gigabytes). This can take long time depending on your hardware. You can find information about other supported models [here](https://huggingface.co/docs/text-generation-inference/main/en/supported_models#supported-models).

## How to use the chatbot  <span id="HowToUse"><span>

You can find the chatbot here: [http://localhost:7860](http://localhost:7860)

## How to develop the code further

To make changes to the code and start the servers with the new changes applied:
1. ```docker compose down```
2. Check out a feature branch: ```git checkout -b <what you want to call your branch>```
3. Make your code changes
4. ```docker build . -t application```
5. ```docker-compose up --detach```
6. See [How to use](#HowToUse)
7. If you are happy with your changes and want to share to the group, commit and push: ```git commit -am "<description of you code changes>"; git push --set-upstream origin <what you called your branch>```
8. When pushing further code you can omit ```--set-upstream origin <what you called your branch>``` from the command above
