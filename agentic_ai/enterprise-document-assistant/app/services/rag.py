from app.llm import get_llm
from app.prompts import RAG_PROMPT
from app.services.retrieval import build_context, retrieve_documents
from app.services.source_extractor import extract_sources
from langchain_core.documents import Document
from typing import Any

def ask_question(msg: str) -> dict[str, Any]:
    documents: list[Document] = retrieve_documents(msg)
    context: str = build_context(documents)
    llm = get_llm()
    chain = RAG_PROMPT | llm
    response = chain.invoke({
        "context": context,
        "question": msg
    })
    sources: list[dict[str, Any]] = extract_sources(documents)

    return {
        "answer": response.text,
        "sources": sources
    }