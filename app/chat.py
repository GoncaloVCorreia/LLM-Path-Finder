from app.embeddings import get_embedding_model
from app.vectorstore import query_vectorstore
from app.llm_client import llm
from app.model import FileSearchResult
from app.prompts import build_system_prompt
import json

def ask_llm(user_query):
    embedding_model = get_embedding_model()
    query_embedding = embedding_model.embed_query(user_query)

    docs, metas = query_vectorstore(query_embedding)

    system_prompt = build_system_prompt(docs, metas)

    llm_response = llm(system_prompt, user_query)

    try:
        content = llm_response.strip()
        parsed_items = json.loads(content)
        results = [FileSearchResult(**item) for item in parsed_items]

        if results:
            for result in results:
                print(f"Confidence Score: {result.score}")
                print(f"Path: {result.path}")
                print(f"Justification: {result.justification}")
                print("-" * 40)
        else:
            print("Not related.")

    except Exception as e:
        print("Failed to parse response:", e)
        print("Raw model output:\n", content)
