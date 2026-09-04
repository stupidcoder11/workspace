from langchain_google_genai import GoogleGenerativeAIEmbeddings

def get_embeddings() -> GoogleGenerativeAIEmbeddings:
    return GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")