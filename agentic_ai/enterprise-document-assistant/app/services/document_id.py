import hashlib
from pathlib import Path

def generate_document_id(file_path: str) -> str:
    path = Path(file_path)
    content: bytes = path.read_bytes()

    return hashlib.sha256(content).hexdigest()