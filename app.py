import gradio as gradio
import os
from huggingface_hub import AsyncInferenceClient
from rag_engine import similarity_search, process_documents

os.write(1,b'Loading LLM.\n')

vertical_list = process_documents()
os.write(1,b'INFO :::::: Step 3-1\n')
tgi_client = AsyncInferenceClient(model='http://model:80')
os.write(1,b'INFO :::::: Step 3-1-1\n')

async def inference(message, history):
    os.write(1,b'INFO :::::: xxxxxxx3-2-1\n')
    content=similarity_search(message, 1)
    os.write(1,b'INFO :::::: Step 3-2-1\n')
    message = content + " " + message 
    partial_message = ""
    os.write(1,b'INFO :::::: Step 3-2-2\n')
    async for token in await tgi_client.text_generation(message, max_new_tokens=2000, stream=True):
        partial_message += token
        os.write(1,b'INFO :::::: Step 3-2-3\n')
        yield partial_message

os.write(1,b'INFO :::::: Step 4-1-1\n')

tgi_chatbot = gradio.ChatInterface(
    inference,
    chatbot=gradio.Chatbot(height=550, placeholder="Hello, you can now ask questions about the following documents: \n" + vertical_list),
    textbox=gradio.Textbox(placeholder="Ask your question here!", container=False, scale=7),
    retry_btn="Retry",
    clear_btn="Clear",
).queue().launch(debug=True, show_api=True)
