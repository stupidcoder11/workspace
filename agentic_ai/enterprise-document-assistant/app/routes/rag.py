from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from app.schemas import AskRequest, AskResponse, UploadResponse
from app.services.rag import ask_question
from app.services.file_handler import save_upload_file
from app.services.ingestion import ingest_pdf

router = APIRouter()


@router.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    answer: str = ask_question(request.question)

    return AskResponse(answer=answer)

@router.post("/upload-document", response_model=UploadResponse)
def upload_documents(file: UploadFile = File(...)):
    file_path: str = save_upload_file(file)
    chunks: int = ingest_pdf(file_path)

    return UploadResponse(
        message="Document uploaded successfully.",
        chunks_stored=chunks
    )