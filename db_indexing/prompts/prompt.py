from langchain.prompts import PromptTemplate

file_summary_prompt = PromptTemplate(
    input_variables=["content"],
    template="""
You are an expert in summarizing code, documents, and configurations with high fidelity and clarity.

Your task is to generate a concise, human-readable summary of the given file content that preserves **key actions, functions, or topics**. 

 The summary will be used in a semantic search engine where users might ask things like:
- “Find the file where I draw a toxic symbol using turtle graphics”
- “Find the PDF where I wrote about birds eating bees”

Therefore, your summary must **retain specific behaviors, themes, and terminology** that could later be searched.

Do not omit:
- Important function names or logic (e.g., drawing shapes, scraping data)
- File purpose or topic (e.g., user login system, invoice generation, poem about cats)

Avoid:
- Redundant boilerplate
- Line-by-line explanations

Only return the **pure summary text**. No formatting. No markdown. 
Only return the pure summary text, ALWAYS followed by a "keywords:" field with relevant search terms (comma-separated). Don't repeat keywords.

Content:
\n
{content}
""",
)
