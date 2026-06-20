import chromadb

client = chromadb.Client()
collection = client.create_collection("resume_db")


def add_chunks(chunks, embeddings):
    ids = [f"id_{i}" for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )


def search_similar(query_embedding):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    return results["documents"][0]