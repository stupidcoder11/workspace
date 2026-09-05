from app.llm import get_llm
from app.prompts import RAG_PROMPT
from app.services.retrieval import build_context, retrieve_documents
from app.services.source_extractor import build_sources_from_citations
from app.services.citation_parser import extract_citations
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
    citations: list[int] = extract_citations(response.text)
    sources: list[dict[str, Any]] = build_sources_from_citations(citations, documents)

    return {
        "answer": response.text,
        "sources": sources
    }