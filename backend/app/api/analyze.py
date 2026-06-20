from fastapi import APIRouter
from app.services.resume_analyzer import analyze_resume

router = APIRouter()

@router.post("/analyze")

def analyze():

    sample_resume = """
    Python
    Machine Learning
    FastAPI
    """

    result = analyze_resume(
        sample_resume
    )

    return result