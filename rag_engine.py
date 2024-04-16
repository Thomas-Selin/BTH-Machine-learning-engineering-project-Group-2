from curses import meta
import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

db = None

def process_documents():
    os.write(1,b'INFO ::: Starting to process documents\n')
    os.write(1,b'INFO :::::: Step 1: Loading PDFs\n')
    pdf_folder_path = "./documents/"
    loader = PyPDFDirectoryLoader(pdf_folder_path)
    os.write(1,b'INFO :::::: Step 2\n')
    data = loader.load()
    os.write(1,b'INFO :::::: Step 3\n')
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=20)
    os.write(1,b'INFO :::::: Step 4\n')
    documents = text_splitter.split_documents(data)
    os.write(1,b'INFO :::::: Step 5\n')
    print("Documents")
    print(documents)
    print("Metadata")
    os.write(1,b'INFO :::::: Step 6\n')
    filenames = [doc.metadata['source'].split('/')[-1] for doc in documents]
    os.write(1,b'INFO :::::: Step 7\n')
    vertical_list = '\n'.join(filenames)
    os.write(1,b'INFO :::::: Step 8\n')
    print("Vertical List")
    print(vertical_list)
    os.write(1,f'INFO ::: The following documents were loaded: "{vertical_list}"\n'.encode())
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    os.write(1,b'INFO :::::: Step 8\n')

# load it into Chroma
    global db
    os.write(1,b'INFO :::::: Step 9\n')
    db = Chroma.from_documents(documents, embedding_function)
    os.write(1,b'INFO :::::: Step 10\n')
    return vertical_list


# Uncomment the following 2 lines to print the documents to terminal
# os.write(1,b'Print the loaded documents\n')
# print(documents)

# os.write(1,b'INFO ::: Starting to process documents and adding to database\n')
# split it into chunks
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# docs = text_splitter.split_documents(documents)

# create the open-source embedding function

 
def similarity_search(query, k=1):
    os.write(1,b'INFO ::::::___A_S_A_S_A\n')
    os.write(1,f'INFO ::: Starting similarity search for query: "{query}"'.encode())
    os.write(1,b'\n')
    os.write(1,b'INFO :::::: Step 2-2\n')
    docs = db.similarity_search(query, k=1)

    # print results
    source = docs[0].metadata['source']
    content = docs[0].page_content
    os.write(1, f'INFO ::: The document: "{source}" was found to be most similair. The content of that file is: "{content}", \n'.encode())
    os.write(1,b'\n')
    return content

# def sendPrompt(prompt):
#     global llm
#     response = llm.invoke(prompt)
#     return response


