from app.services.llm_services import ask_llm

def generate_questions(role):

    prompt = f"""
    Generate 10 interview questions
    for {role}
    """

    return ask_llm(prompt)