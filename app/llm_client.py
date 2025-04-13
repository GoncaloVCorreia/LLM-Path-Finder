import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def llm(system_prompt, user_query):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # or "llama3-70b-8192" "mistral-saba-24b"
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query},
        ],
        temperature=0.3,
        max_tokens=1000,
    )
    return response.choices[0].message.content
