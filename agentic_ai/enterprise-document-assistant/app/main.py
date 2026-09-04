from fastapi import FastAPI
from app.routes.rag import router as rag_router

app = FastAPI(
    title="Enterprise Document Assistant"
)

app.include_router(rag_router)