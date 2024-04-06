from langchain_community.llms import Ollama
import streamlit as st
import os

os.write(1,b'Loading LLM.\n')

llm = Ollama(model="phi", base_url="http://0.0.0.0:11434", verbose=True)

os.write(1,b'FINISHED (Loading LLM).\n')

def sendPrompt(prompt):
    global llm
    response = llm.invoke(prompt)
    return response



st.title("Chat with Ollama")
if "messages" not in st.session_state.keys(): 
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question !"}
    ]

if prompt := st.chat_input("Your question"): 
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: 
    with st.chat_message(message["role"]):
        st.write(message["content"])
        
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = sendPrompt(prompt)
            print(response)
            st.write(response)
            message = {"role": "assistant", "content": response}
            st.session_state.messages.append(message) 
