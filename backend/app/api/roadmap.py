from fastapi import APIRouter
from app.services.roadmap_service import generate_roadmap

router = APIRouter()

@router.get("/roadmap/{role}")

def roadmap(role):

    return {
        "roadmap":
        generate_roadmap(role)
    }