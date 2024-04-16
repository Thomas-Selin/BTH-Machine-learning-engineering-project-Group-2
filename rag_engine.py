import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
# from langchain.text_splitter import RecursiveCharacterTextSplitter

chunk_size = int(os.environ.get('CHUNK_SIZE', '200'))
chunk_overlap = int(os.environ.get('CHUNK_OVERLAP', '20'))

db = None

def process_documents():
    os.write(1,b'INFO ::: Starting to process documents\n')
    pdf_folder_path = "./documents/"
    loader = PyPDFDirectoryLoader(pdf_folder_path)
    data = loader.load()
    # print(f'Data: {data}')
    # text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    text_splitter = CharacterTextSplitter(
        separator=".",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )
    documents = text_splitter.split_documents(data)

    filenames = [doc.metadata['source'].split('/')[-1] for doc in data]
    vertical_list = '\n'.join(filenames)

    os.write(1,f'INFO ::: The following documents were loaded: \n{vertical_list}\n'.encode())
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    
    global db
    db = Chroma.from_documents(documents, embedding_function)
    return vertical_list
 
def similarity_search(query, k=1):
    os.write(1, f'INFO ::: Starting similarity search for query: "{query}"\n'.encode())
    docs = db.similarity_search(query, k=1)

    source = docs[0].metadata['source']
    content = docs[0].page_content
    os.write(1, f'INFO ::: The document: "{source}" was found to be most similair.\n'.encode())
    return source, content
