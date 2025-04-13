from app.chat import ask_llm
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
if __name__ == "__main__":
    query = "where did i put my input files for scenario 2, how many are there?"
    ask_llm(query)
