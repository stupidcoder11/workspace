from app.services.ingestion import ingest_pdf

total_chunks: int = ingest_pdf("documents/company_policy.pdf")
print(f"Stored {total_chunks} in Chroma")