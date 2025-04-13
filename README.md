# Local RAG Pipeline – "Where Did I Put That File?"

This project is a local **Retrieval-Augmented Generation (RAG)** pipeline built to help users locate files and folders using natural language. If you ever find yourself asking:

> “Where did I put my medical results?”    
> “What folder has my notes from the First Semestre?”

This tool uses an LLM to **search your local documents** semantically, even if you don’t remember file names or folder locations.

---

## 🎯 Project Goal

The aim is simple:  
Let the user set a root directory, then enable an LLM to **understand the structure and content of your files and folders**—and answer questions like a personal file assistant.

This is especially useful if:
- You have thousands of scattered files.
- You remember what something is *about*, not where it is.
- You want to use natural language to navigate your digital world.

---

## Features

- **File Crawler & Reader**: Walks your directories and reads files for indexing.
- **Document Descriptor**: Summarizes the pre-defined file types into compact metadata descriptions.
- **Embedder**: Generates vector embeddings.
- **Parallel Embedding**: Files are embedded in parallel using a configurable number of workers.
- **Vectorstore Integration**: Stores and retrieves file embeddings (e.g., ChromaDB).
- **LLM Summarization Chain**: Generates natural language responses to queries, powered by local or API-hosted models.


The variables like token limits, batch sizes, or number of parallel workers can (and should) be adjusted depending on your hardware, model constraints and your user Tier.

---

## ⚙️ Configuration

Edit `config.py` to set:

- `CHUNK_SIZE`, `CHUNK_OVERLAP`: for document chunking.
- `CONTEXT_TOKEN_LIMIT`: max tokens allowed for your LLM context window.
- `MAX_PARALLEL_WORKERS`: number of threads used for embedding. Increase if your system or token/minute quota allows.
- `ROOT_DIR`: The main root for crawling.
- `EXCLUDE_DIRS`: Directories and file types you don't want to crawl

---

## How to Run

1. python index.py (to index all your files and directories inside the main root)
2. python main.py (you can define the user requery in this file) 

