import os
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

groq_llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",#mistral-saba-24b
    temperature=0.3,
    max_tokens=512,
)
    







