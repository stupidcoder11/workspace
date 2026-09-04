from dotenv import load_dotenv
from app.core.config import settings
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def get_llm() -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model=settings.GEMINI_MODEL, 
        temperature=0.2
    )
