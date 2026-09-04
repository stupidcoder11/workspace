from app.services.vectorstore import get_vectorstore
from langchain_core.documents import Document

def retrieve_documents(question: str, top_k: int = 4) -> list[Document]:
    vectorstore = get_vectorstore()
    return vectorstore.similarity_search(question, k=top_k)

def build_context(documents: list[Document]) -> str:
    context: str = "\n\n".join(d.page_content for d in documents)
    return context