# Test-APP - Group 2 ML @ BTH 
## How to start

1. Download and start [Docker Desktop](https://www.docker.com/products/docker-desktop/)

2. Build the application image

```
docker build . -t application
```

3. Start the servers. (See docker-compose.yml file. Both container for serving the model and container for the application will be started)
   
```
docker-compose up --detach
```

4. Download and set up a model of your choice (and your hardware can handle). In this example the model is named "phi".

In another terminal window:
```
docker exec -it model-container ollama run phi
```

## How to use

You can find the chatbot here: [http://localhost:8501](http://localhost:8501)

## Various non essential information
For testing (for example other models) you can communicate directly with the Ollama API via [http://localhost:11434](http://localhost:11434) in the way described here: [Ollama API documentation](https://github.com/ollama/ollama/blob/main/docs/api.md)


# TODO Thomas

- skriv ut freeze versionerna
