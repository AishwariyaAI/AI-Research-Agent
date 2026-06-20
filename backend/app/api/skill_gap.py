from fastapi import APIRouter
from app.services.skill_gap_service import find_skill_gap

router = APIRouter()

@router.post("/skill-gap")

def skill_gap():

    resume_text = """
    Python
    Pandas
    NumPy
    """

    job_text = """
    Python
    Docker
    AWS
    LangChain
    """

    gaps = find_skill_gap(
        resume_text,
        job_text
    )

    return {
        "missing_skills": gaps
    }