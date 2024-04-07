import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

os.write(1,b'INFO ::: Loading PDFs\n')
pdf_folder_path = "documents/"
loader = PyPDFDirectoryLoader(pdf_folder_path) 
data = loader.load()

# Uncomment the following 2 lines to print the data
# os.write(1,b'Print the loaded data\n')
# print(data)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=20)
documents = text_splitter.split_documents(data)

# Uncomment the following 2 lines to print the documents
# os.write(1,b'Print the loaded documents\n')
# print(documents)

# persist_directory="/tmp/db"

os.write(1,b'INFO ::: Starting to process documents and adding to database\n')
# split it into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# load it into Chroma
db = Chroma.from_documents(documents, embedding_function)

query = "yellow"
os.write(1,f'INFO ::: Starting similarity search for query: "{query}"'.encode())
os.write(1,b'\n')

docs = db.similarity_search(query, k=1)

# print results
source = docs[0].metadata['source']
content = docs[0].page_content
os.write(1, f'INFO ::: The document: "{source}" was found to be most similair. The content of that file is: "{content}", \n'.encode())
os.write(1,b'\n')
