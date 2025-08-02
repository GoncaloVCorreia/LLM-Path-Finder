from langchain.output_parsers import PydanticOutputParser
from langchain.schema.runnable import RunnableLambda
from llms.llm import groq_llm
#from llm.llm import local_llm
from  prompts.prompt import file_summary_prompt
import time
import requests
from typing import Optional
import tiktoken


summary_chain = (
    file_summary_prompt
    | groq_llm
    | RunnableLambda(lambda x: x.content)
)

MAX_TOKENS_FOR_SUMMARY = 4800  # Leave buffer for prompt


def estimate_tokens(text, model_name = "gpt-3.5-turbo"):
    try:
        enc = tiktoken.encoding_for_model(model_name)
    except Exception:
        enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))

def truncate_by_tokens(text, max_tokens=MAX_TOKENS_FOR_SUMMARY, model_name="gpt-3.5-turbo"):
    try:
        enc = tiktoken.encoding_for_model(model_name)
    except:
        enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    truncated_tokens = tokens[:max_tokens]
    return enc.decode(truncated_tokens)

def safe_summarize_with_groq(prompt) :
    try:
        # Truncate if too long
        print(estimate_tokens(prompt))
        if estimate_tokens(prompt) > MAX_TOKENS_FOR_SUMMARY:
            print("Truncating long input to avoid context overflow...")
            prompt = truncate_by_tokens(prompt)
            print(estimate_tokens(prompt))
            print("Truncation Finished")
        result = summary_chain.invoke({"content": prompt})
        return result
       
    except Exception as e:
        return f"[LLM Summary Failed: {e}]"

#Example of replacing the summarize function
def summarize_file_content(content) :
    print("🔍 Summarizing with Groq...")
    return safe_summarize_with_groq(content)
