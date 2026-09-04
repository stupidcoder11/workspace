from app.llm import get_llm
from app.prompts import RAG_PROMPT
from app.services.retrieval import build_context

def ask_question(msg: str) -> str:
    context: str = build_context(msg)
    llm = get_llm()
    chain = RAG_PROMPT | llm
    response = chain.invoke({
        "context": context,
        "question": msg
    })
    return str(response.content)