from app.llm import get_llm
from app.prompts import RAG_PROMPT


llm = get_llm()

chain = RAG_PROMPT | llm

response = chain.invoke({
    "context": "FastAPI is a Python web framework used for building APIs.",
    "question": "What is FastAPI?"
})

print(response.content)