from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from connections import api_key,mongodb_uri,collection,db

def get_pdf_text(pdf): 
    text = ""
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(chunks):
    embedding_method=GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=api_key)
    for chunk in chunks:
        print(chunk)
        embedding=embedding_method.embed_documents([chunk])
        collection.insert_one({
            "text":chunk,
            "embedding":embedding[0]
        })

def pdftext_to_vector_single(pdf):  
    text = get_pdf_text(pdf)
    chunks_data = get_text_chunks(text)
    get_vector_store(chunks_data)
    print(f'PDF text converted to vector')

def get_query_embedding(query):
    embedding_method = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
    embedding = embedding_method.embed_documents([query])
    return embedding[0]