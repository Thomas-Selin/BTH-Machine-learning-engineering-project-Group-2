import os
import gradio as gradio
from huggingface_hub import AsyncInferenceClient
from rag_engine import similarity_search, process_documents

vertical_list = process_documents()
tgi_client = AsyncInferenceClient(model='http://model:80')
max_new_tokens = int(os.environ.get('MAX_NEW_TOKENS', '2000'))

async def inference(message, history):
    source, content=similarity_search(message, 1)
    message = content + " " + message 
    partial_message = "Answer is based on the document: " + source + "\n"
    async for token in await tgi_client.text_generation(message, max_new_tokens=max_new_tokens, stream=True):
        partial_message += token
        yield partial_message

tgi_chatbot = gradio.ChatInterface(
    inference,
    chatbot=gradio.Chatbot(height=550, placeholder="Hello, you can now ask questions about the following documents: \n" + vertical_list),
    textbox=gradio.Textbox(placeholder="Ask your question here", container=False, scale=7),
    clear_btn="Clear",
).queue().launch(debug=True, show_api=True)
