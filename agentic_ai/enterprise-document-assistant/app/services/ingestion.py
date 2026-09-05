from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.services.vectorstore import get_vectorstore
from app.services.document_id import generate_document_id
from app.core.config import settings
from app.core.logger import get_logger
from pathlib import Path

logger = get_logger(__name__)

def load_file(file_path: str) -> list[Document]:
    loader = PyPDFLoader(file_path)
    return loader.load()

def split_documents(documents: list[Document]) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(chunk_size=settings.CHUNK_SIZE, chunk_overlap=settings.CHUNK_OVERLAP)
    chunks: list[Document] = splitter.split_documents(documents)
    logger.info(f"Generated {len(chunks)} chunks.")
    return chunks

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
        logger.info(f"Ingestion skipped to avoid document (document_id={document_id}) duplicity")
        return 0

    logger.info(f"New document (document_id={document_id}) detected, ingestion begins")
    
    vectorstore.add_documents(
        documents=chunks,
        chunk_ids=chunk_ids
    )

    return len(chunks)