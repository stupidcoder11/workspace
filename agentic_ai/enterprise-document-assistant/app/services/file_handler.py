from pathlib import Path
from fastapi import UploadFile

DOCUMENTS_DIR = Path("documents")
DOCUMENTS_DIR.mkdir(exist_ok=True)

def save_upload_file(file: UploadFile) -> str:
    if not file.filename:
        raise ValueError("Uploaded file must have a filename.")

    file_path = DOCUMENTS_DIR / file.filename
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return str(file_path)