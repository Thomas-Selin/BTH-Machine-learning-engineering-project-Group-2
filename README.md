# RAG Chat Bot - Group 2 Machine learning engineering @ BTH 

This project has been a part of the university course Machine learning engineering at Blekinge Institute of Technology during 2024.

This project has 4 main parts:
1. A server that serves the language model. The server uses the ```ghcr.io/huggingface/text-generation-inference:1.4``` image.
2. ```app.py```: Code for an gradio application that provides a chatbot frontend for chatting with the language model. ```app.py``` also connects to the language model and the logic in ```rag_engine.py```.
3. ```rag-engine.py```: This code implements RAG. Documents in the ```documents``` folder (either in PDF or Markdown format) are preprocessed and split into chunks and stored in a vector database. When a question is asked to the chatbot, logic is triggered that searches through the data for the content that most relates to the users question. This is done by a geometric mathematical algorithm using the chunk vectors. Chunks of text in the most related document is being provided to the language model together with the users question. Reference to which document was used as context is being provided to the chatbot frontend.
4. Vector database, used to store the the vectorized text chunks and for finding the vectors that to the highest degree relates to the users question.
   

## Choosing the language model to run

Using our set up, you can decide between many different kinds of language models. Specified as the default model (in the docker-compose.yml file) is **stabilityai/stablelm-2-zephyr-1_6b** which is a small model that can be run on many PC:s and Mac:s. If you have problems getting the model-server to run with this model, you can use the even smaller **bigscience/mt0-small** model, but the quality of the chatbots answers will be unimpressive. 

If your computer has more resources, we recommend that you test the **microsoft/phi-2** model for improved chatbot answer quality.

You can find information about other supported models [here](https://huggingface.co/docs/text-generation-inference/main/en/supported_models#supported-models), although you can run many other models as well, but they are not offically supported by the Text Generation Inference framework.

## How to start the chatbot

1. Clone this repo: ```git clone git@github.com:ttechstuff/group2-ML-app-v1.git; cd group2-ML-app-v1```

2. Download, install, and start [Docker Desktop](https://www.docker.com/products/docker-desktop/).

3. Build the application image.

```
docker build . -t application
```

4. NORMALLY NOT NECESSARY: Some hugging-face models can only be downloaded if you provide a HUGGING_FACE_HUB_TOKEN with read permission. This requires a free huggingface account. You can provide the HUGGING_FACE_HUB_TOKEN in the docker-compose.yml file.

5. Start the servers.

```
docker-compose up --detach
```

As the servers starts, the language model will be downloaded (if not already downloaded) and set up. This can take long time depending on your hardware, internet speed and choice of model.

## How to use the chatbot

You can find the chatbot here: [http://localhost:7860](http://localhost:7860)

## How to develop the code further

To make changes to the code and start the servers with the new changes applied:
1. ```docker compose down```
2. Check out a feature branch: ```git checkout -b <what you want to call your branch>```
3. Make your code changes
4. ```docker build . -t application```
5. ```docker-compose up --detach```
6. See "How to use the chatbot" section above
7. If you are happy with your changes and want to share to the group, commit and push: ```git commit -am "<description of you code changes>"; git push --set-upstream origin <what you called your branch>```
8. When pushing further code you can omit ```--set-upstream origin <what you called your branch>``` from the command above
