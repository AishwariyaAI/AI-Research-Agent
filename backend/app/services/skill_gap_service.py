def extract_skills(text):

    skills_db = [
        "python",
        "numpy",
        "pandas",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "docker",
        "aws",
        "sql",
        "langchain",
        "rag",
        "fastapi"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def find_skill_gap(resume_text, job_text):

    resume_skills = set(
        extract_skills(resume_text)
    )

    job_skills = set(
        extract_skills(job_text)
    )

    missing_skills = list(
        job_skills - resume_skills
    )

    return missing_skills