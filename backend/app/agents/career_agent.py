from app.services.rag_service import retrieve_context
from app.services.llm_services import ask_llm

def career_agent(query):

    context = retrieve_context(query)

    prompt = f"""
    Resume Information:

    {context}

    User Question:

    {query}

    Answer using resume context.
    """

    return ask_llm(prompt)