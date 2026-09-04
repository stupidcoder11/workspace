from pydantic import BaseModel

class AskRequest(BaseModel):
    question: str

class SourceResponse(BaseModel):
    document: str
    page: int
    chunk_id: str

class AskResponse(BaseModel):
    answer: str
    sources: list[SourceResponse]

class UploadResponse(BaseModel):
    message: str
    chunks_stored: int