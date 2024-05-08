import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
# from langchain.text_splitter import RecursiveCharacterTextSplitter

chunk_size = int(os.environ.get('CHUNK_SIZE', '200'))
chunk_overlap = int(os.environ.get('CHUNK_OVERLAP', '20'))

db = None

def process_documents():
    document_folder_path = "./documents/"
    text_splitter = CharacterTextSplitter(
        separator=".",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )
    docs = []
    filenames = []
    global db
    for root, dirs, files in os.walk(document_folder_path):
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
    vertical_list = '\n'.join(filenames)
        
    os.write(1,f'INFO ::: The following documents were loaded: \n{vertical_list}\n'.encode())
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    
    db = Chroma.from_documents(documents, embedding_function)
    return vertical_list
 
def similarity_search(query, k=1):
    os.write(1, f'INFO ::: Starting similarity search for query: "{query}"\n'.encode())
    docs = db.similarity_search(query, k=1)

    source = docs[0].metadata['source']
    content = docs[0].page_content
    os.write(1, f'INFO ::: The document: "{source}" was found to be most similair.\n'.encode())
    return source, content
