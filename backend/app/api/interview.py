from fastapi import APIRouter
from app.services.interview_service import generate_questions

router = APIRouter()

@router.get("/interview/{role}")

def interview(role):

    questions = generate_questions(
        role
    )

    return {
        "questions": questions
    }