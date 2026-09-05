"""
Goal
----
- Remove duplicates
- Produce clean citations
- Keep RAG layer simple
"""
from langchain_core.documents import Document
from typing import Any

def build_sources_from_citations(citations: list[int], documents: list[Document]) -> list[dict[str, Any]]:
    sources: list[dict[str, Any]] = []
    seen: set[tuple[Any | None, Any | None]] = set()

    for citation in citations:
        doc = documents[citation - 1]
        source = {
            "document": doc.metadata.get("document_name"),
            "page": doc.metadata.get("page"),
            "chunk_id": doc.metadata.get("chunk_id")
        }
        key = (source["document"], source["page"])
        if key not in seen:
            seen.add(key)
            sources.append(source)

    return sources
