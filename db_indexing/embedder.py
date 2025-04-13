from langchain_huggingface import HuggingFaceEmbeddings
from tqdm import tqdm

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'batch_size': 32, 'normalize_embeddings': True}
)

def embed_documents(docs):
    texts = [doc.page_content for doc in docs]
    metadatas = [doc.metadata for doc in docs]
    embeddings = []
    with tqdm(total=len(texts), desc="Embedding documents", unit="doc") as pbar:
        for i in range(0, len(texts), 32):
            batch = texts[i:i+32]
            embedded = embedding_model.embed_documents(batch)
            embeddings.extend(embedded)
            pbar.update(len(batch))
    return embeddings, texts, metadatas
