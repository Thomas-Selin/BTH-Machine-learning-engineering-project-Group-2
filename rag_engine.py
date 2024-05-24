import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_text_splitters import SpacyTextSplitter


chunk_size = int(os.environ.get('CHUNK_SIZE', '200'))
chunk_overlap = int(os.environ.get('CHUNK_OVERLAP', '20'))

db = None

def process_documents():
    document_folder_path = "documents/"
    text_splitter = SpacyTextSplitter(chunk_size=1000)
    docs = []
    filenames = []
    global db
    for root, dir, files in os.walk(document_folder_path):
        for name in files:
            if name.endswith((".pdf")):
                loader = PyMuPDFLoader(os.path.join(root, name))
            elif name.endswith((".md")):
                loader = UnstructuredMarkdownLoader(os.path.join(root, name))
            else:
                continue
            docs.extend(loader.load())
            filenames += name
    documents = text_splitter.split_documents(docs)
    filenames = [doc.metadata['source'].split('/')[-1] for doc in docs]
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
    os.write(1, f'INFO ::: The document: "{source}" was found to be most similar.\n'.encode())
    return source, content
