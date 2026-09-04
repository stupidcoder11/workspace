from langchain_chroma import Chroma

from app.services.embeddings import get_embeddings
from app.core.config import settings

PERSIST_DIRECTORY = settings.CHROMA_PERSIST_DIRECTORY

def get_vectorstore() -> Chroma:
    embeddings = get_embeddings()
    return Chroma(
        collection_name=settings.CHROMA_COLLECTION_NAME,
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings,
    )