from app.services.skill_gap_service import extract_skills

def analyze_resume(text):

    skills = extract_skills(text)

    return {
        "skills": skills,
        "total_skills": len(skills)
    }