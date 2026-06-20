from fastapi import APIRouter
from pydantic import BaseModel

from app.services.embeddings import get_embedding
from app.services.vector_db import search_similar
from app.services.llm import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str


@router.post("/chat")
def chat(request: ChatRequest):

    # Step 1: Embed query
    query_embedding = get_embedding(request.prompt)

    # Step 2: Retrieve resume context
    context = search_similar(query_embedding)

    # Step 3: Build professional prompt
    final_prompt = f"""
Resume Context:
{context}

User Question:
{request.prompt}

Give a structured career-focused answer.
"""

    # Step 4: Call LLM (REAL AI)
    answer = generate_response(final_prompt)

    return {
        "question": request.prompt,
        "context_used": context,
        "answer": answer
    }