from chromadb import PersistentClient

def query_vectorstore(query_embedding):
    chroma_client = PersistentClient(path="./db_indexing/vector_index_db")
    collection = chroma_client.get_or_create_collection(name="file_index")

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=10,
        include=["documents", "metadatas"]
    )
    return results["documents"][0], results["metadatas"][0]
