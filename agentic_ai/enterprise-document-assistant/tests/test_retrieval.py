from app.services.retrieval import retrieve_documents
from langchain_core.documents import Document

question: str = "What's the leave policy?"
documents: list[Document] = retrieve_documents(question)

print(f"Retrieved documents: {len(documents)}")

for pos, document in enumerate(documents, start=1):
    print(f"\n---Document {pos}---")
    print(document.page_content)
    print("Metadata:", document.metadata)