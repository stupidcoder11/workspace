from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from app.schemas import AskRequest, AskResponse, UploadResponse
from app.services.rag import ask_question
from app.services.file_handler import save_upload_file
from app.services.ingestion import ingest_pdf
from app.core.logger import get_logger

logger = get_logger(__name__)

router = APIRouter(tags=["RAG API"])

@router.post("/ask", response_model=AskResponse, description="This endpoint takes user queries as input and provides a response to it.")
def ask(request: AskRequest):
    logger.info(f"Question received: {request.question}")
    try:
        response = ask_question(request.question)
        logger.info("Answer generated successfully.")
        return response
    except Exception:
        logger.exception("Answer failed to generate.") # automatically includes stack trace
        raise

@router.post("/upload-document", response_model=UploadResponse)
def upload_documents(file: UploadFile = File(...)):
    logger.info(f"Document upload requested: {file.filename}")
    file_path: str = save_upload_file(file)
    chunks: int = ingest_pdf(file_path)
    logger.info(f"File stored successfully: {file_path}")

    return UploadResponse(
        message="Document uploaded successfully.",
        chunks_stored=chunks
    )