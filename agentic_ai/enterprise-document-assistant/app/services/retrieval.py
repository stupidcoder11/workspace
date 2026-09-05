from app.services.vectorstore import get_vectorstore
from app.core.logger import get_logger
from langchain_core.documents import Document

logger = get_logger(__name__)

def retrieve_documents(question: str, top_k: int = 4) -> list[Document]:
    vectorstore = get_vectorstore()
    retrieved_documents: list[Document] = vectorstore.similarity_search(question, k=top_k)
    logger.info(f"Retrieved {len(retrieved_documents)} chunks.")
    for doc in retrieved_documents:
        logger.info(
            (
                f"Retrieved "
                f"{doc.metadata.get("document_name")} "
                f"page={doc.metadata.get("page")} "
                f"chunk={doc.metadata.get("chunk_id")}"
            )
        )
    return retrieved_documents

def build_context(documents: list[Document]) -> str:
    context: str = "\n\n".join(
        f"{pos}\n{doc.page_content}" for pos, doc in enumerate(documents, start=1)
    )
    return context