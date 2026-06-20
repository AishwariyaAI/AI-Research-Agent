from fastapi import APIRouter
from app.services.ats_service import calculate_ats_score

router = APIRouter()

@router.post("/ats")

def ats():

    resume = """
    Python Pandas NumPy
    """

    job = """
    Python Pandas Docker AWS
    """

    score = calculate_ats_score(
        resume,
        job
    )

    return {
        "ats_score": score
    }