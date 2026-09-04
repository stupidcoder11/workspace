import os
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    GOOGLE_API_KEY: str = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL")
    CHROMA_COLLECTION_NAME: str = os.getenv("CHROMA_COLLECTION_NAME")
    CHROMA_PERSIST_DIRECTORY: str = os.getenv("CHROMA_PERSIST_DIRECTORY")
    CHUNK_SIZE: int = os.getenv("CHUNK_SIZE")
    CHUNK_OVERLAP: int = os.getenv("CHUNK_OVERLAP")

    model_config = (
        SettingsConfigDict(
            env_file=".env",
            extra="ignore"
        )
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()