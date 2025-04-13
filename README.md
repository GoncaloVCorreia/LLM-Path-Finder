# Local RAG Pipeline – "Where Did I Put That File?"

This project is a local **Retrieval-Augmented Generation (RAG)** pipeline built to help users locate files and folders using natural language. If you ever find yourself asking:

> “Where did I put my medical results?”    
> “What folder has my notes from the First Semester?”

This tool uses an LLM to **search your local documents** semantically, even if you don’t remember file names or folder locations.

---

## Project Goal

The aim is simple:  
Let the user set a root directory, then enable an LLM to **understand the structure and content of your files and folders**—and answer questions like a personal file assistant.

This is especially useful if:
- You have thousands of scattered files.
- You remember what something is *about*, not where it is.
- You want to use natural language to navigate your digital world.

---

### Crawl & Describe
Walks through your directories and builds a **metadata layer** by analyzing each file and folder.

### Document Descriptor
For predefined file types like `.py`, `.pdf`, `.docx`, and others, the system **sends their content to an LLM to generate summaries**. These summaries are then stored as part of the file's metadata.

- The **token budget per file** is automatically adjusted based on your selected model and its context length.
- If you're using a model with a smaller token limit, summaries will be shorter or truncated.
- This step enables **semantic search** even when filenames or paths are non-informative.

### Embed & Store
Files and their descriptions are **chunked and embedded into a vector database** for retrieval.

### Parallelized Indexing
Embedding and summarization tasks are done in **parallel**. The number of workers can be increased depending on your computing power or token/minute quota.

### RAG Chat
Chat with a local LLM interface to **retrieve file locations, summaries, or folder structures** using natural language.

Each response is structured and returned as a `FileSearchResult`, which includes:

- `score` (0–100): A confidence score estimating how well the result matches your query.
- `path`: The full path to the relevant file or folder.
- `justification`: A brief explanation of **why this item was selected**, based on content, metadata, or semantic relevance.

This makes the output easy to parse, display, or integrate into a larger system. The LLM may return more than one file.

### Token-Aware
The variables like token limits, batch sizes, or number of parallel workers can (and should) be adjusted depending on your hardware, model constraints and user Tier.

---

## Configuration

Edit `config.py` to set:

- `CHUNK_SIZE`, `CHUNK_OVERLAP`: for document chunking.
- `CONTEXT_TOKEN_LIMIT`: max tokens allowed for your LLM context window.
- `MAX_PARALLEL_WORKERS`: number of threads used for embedding. Increase if your system or token/minute quota allows.
- `ROOT_DIR`: The main root for crawling.
- `EXCLUDE_DIRS`: Directories and file types you don't want to crawl

---

## How to Run

1. python index.py (to index all your files and directories inside the main root)
2. python main.py (you can define the user query in this file) 

