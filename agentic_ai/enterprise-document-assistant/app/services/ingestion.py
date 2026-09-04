from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.services.vectorstore import get_vectorstore
from app.services.document_id import generate_document_id
from app.core.config import settings
from pathlib import Path

def load_file(file_path: str) -> list[Document]:
    loader = PyPDFLoader(file_path)
    return loader.load()

def split_documents(documents: list[Document]) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(chunk_size=settings.CHUNK_SIZE, chunk_overlap=settings.CHUNK_OVERLAP)
    return splitter.split_documents(documents)

def ingest_pdf(file_path: str) -> int:
    documents = load_file(file_path)
    chunks: list[Document] = split_documents(documents)

    document_id: str = generate_document_id(file_path)
    chunk_ids = [f"{document_id}_{index}" for index in range(len(chunks))]

    for index, chunk in enumerate(chunks):
        chunk.metadata["document_id"] = document_id
        chunk.metadata["document_name"] = Path(file_path).name
        chunk.metadata["chunk_id"] = chunk_ids[index]

    vectorstore = get_vectorstore()

    # handle duplicates
    existing = vectorstore.get(where={
        "document_id": document_id
    })
    if existing["ids"]:
        print("[Ingestion skipped to avoid document duplicity.]")
        return 0
    
    vectorstore.add_documents(
        documents=chunks,
        chunk_ids=chunk_ids
    )

    return len(chunks)