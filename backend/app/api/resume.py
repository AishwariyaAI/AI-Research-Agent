from fastapi import APIRouter, UploadFile, File

from app.services.pdf_reader import extract_text
from app.services.embeddings import get_embedding
from app.services.vector_db import add_chunks

router = APIRouter()

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    content = await file.read()

    text = extract_text(content)

    # clean chunks
    chunks = [c.strip() for c in text.split("\n") if len(c.strip()) > 10]

    embeddings = [get_embedding(c) for c in chunks]

    add_chunks(chunks, embeddings)

    return {
        "message": "Resume processed successfully",
        "chunks": len(chunks)
    }