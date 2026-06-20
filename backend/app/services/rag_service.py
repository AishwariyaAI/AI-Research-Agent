from app.database.chroma import collection
from app.services.embedding_service import get_embedding

def retrieve_context(query):

    query_embedding = get_embedding(
        query
    )

    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=2
    )

    return results["documents"][0]