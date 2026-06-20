def generate_roadmap(role):

    roadmap = {
        "AI Engineer":[
            "Python",
            "NumPy",
            "Pandas",
            "Machine Learning",
            "Deep Learning",
            "RAG",
            "AI Agents"
        ]
    }

    return roadmap.get(role, [])