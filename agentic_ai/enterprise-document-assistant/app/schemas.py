from pydantic import BaseModel

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    answer: str

class UploadResponse(BaseModel):
    message: str
    chunks_stored: int