from chromadb import PersistentClient
from tqdm import tqdm
from config import CHROMA_PATH, BATCH_SIZE

def save_embeddings_to_chroma(texts, embeddings, metadatas):
    print("💾 Saving to vector database in batches...")
    chroma_client = PersistentClient(path=CHROMA_PATH)
    collection = chroma_client.get_or_create_collection(name="file_index")

    for i in tqdm(range(0, len(texts), BATCH_SIZE), desc="Writing to Chroma", unit="batch"):
        end = min(i + BATCH_SIZE, len(texts))
        collection.add(
            documents=texts[i:end],
            embeddings=embeddings[i:end],
            metadatas=metadatas[i:end],
            ids=[str(j) for j in range(i, end)]
        )
