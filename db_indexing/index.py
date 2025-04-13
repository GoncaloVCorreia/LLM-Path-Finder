from crawler import build_file_queue
from descriptor import describe_all_items
from embedder import embed_documents
from db import save_embeddings_to_chroma

def main():
    jobs = build_file_queue()
    docs = describe_all_items(jobs)
    embeddings, texts, metadatas = embed_documents(docs)
    save_embeddings_to_chroma(texts, embeddings, metadatas)

if __name__ == "__main__":
    main()
