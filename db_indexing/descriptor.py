import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from config import ROOT_DIR
from utils.file_reader import read_file_content, read_docx_text, read_pdf_text
from chain import summarize_file_content
from langchain.schema import Document
import os
from datetime import datetime

def describe_item(path, is_file=True):
    try:
        stats = os.stat(path)
        mod_time = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        size = stats.st_size if is_file else None
        item_type = "file" if is_file else "folder"
        parent_dir = os.path.basename(os.path.dirname(path))
        name = os.path.basename(path)
        ext = os.path.splitext(path)[-1].lower() if is_file else ""
        depth = len(path.replace(ROOT_DIR, "").split(os.sep)) - 1
        is_hidden = name.startswith(".")
        is_executable = os.access(path, os.X_OK) if is_file else False

        description = f"This is a {item_type} named '{name}' located in the '{parent_dir}' directory.\n"
        description += f"Its full path is: {path}.\n"
        if is_file:
            description += f"It has the file extension '{ext}', is {'hidden' if is_hidden else 'visible'}, "
            description += f"and {'is' if is_executable else 'is not'} executable.\n"
            description += f"The file size is {size} bytes, and it was last modified on {mod_time}.\n"
        else:
            description += f"This is a folder at depth {depth} in the directory tree.\n"
            description += f"It {'is' if is_hidden else 'is not'} hidden and was last modified on {mod_time}.\n"

       # Add semantic classification
        if ext in [".jpg", ".jpeg", ".png", ".gif", ".heic"]:
            description += "This is an image file, possibly a personal photo, screenshot, or graphic asset.\n"
        elif ext in [".pdf", ".docx", ".doc", ".txt", ".md"]:
            description += "This is a document file, likely containing written content such as notes, reports, or manuals.\n"
        elif ext in [".mp4", ".mov", ".avi", ".mkv"]:
            description += "This is a video file, possibly a recording, movie, or presentation.\n"
        elif ext in [".mp3", ".wav", ".aac"]:
            description += "This is an audio file, potentially music, recordings, or voice memos.\n"
        elif ext in [".py"]:
            description += "This is a Python source code file.\n"
        elif ext in [".js"]:
            description += "This is a JavaScript file.\n"
        elif ext in [".ts"]:
            description += "This is a TypeScript file.\n"
        elif ext in [".jsx", ".tsx"]:
            description += "This is a React component file.\n"
        elif ext in [".json", ".yaml", ".yml"]:
            description += "This is a structured data/config file.\n"
        elif ext in [".sh", ".bat"]:
            description += "This is a shell or batch script.\n"
        elif ext in [".cpp", ".c", ".h", ".hpp"]:
            description += "This is a C/C++ source or header file.\n"
        elif ext in [".java"]:
            description += "This is a Java file.\n"
        elif ext in [".lock", "package-lock.json", "yarn.lock"]:
            description += "This file manages project dependency versions and should not be manually edited.\n"
            
            
        if ext in [".pdf", ".docx", ".doc", ".txt", ".md",".py", ".js", ".ts", ".tsx", ".jsx", ".cpp", ".c", ".h", ".hpp", ".java"]:
            summary = ""
            if ext == ".pdf":
                print(f"Pdf path {path}")
                file_content=read_pdf_text(path)
            elif ext == ".docx":
                print(f"Docx path {path}")
                file_content = read_docx_text(path)
            else:
                file_content = read_file_content(path)

            if file_content:
                summary = summarize_file_content(file_content)
                print(summary.strip())
            if summary:
                description += f"Summary: {summary.strip()}\n"
    
        return Document(page_content=description.strip(), metadata={"path": path})
    except Exception as e:
        print(f"[!] Failed to process {path}: {e}")
        return None

def describe_all_items(file_jobs):
    docs = []
    with tqdm(total=len(file_jobs), desc="Indexing files and folders", unit="item", file=sys.stdout) as pbar:
        with ThreadPoolExecutor(max_workers=1) as executor:
            futures = {
                executor.submit(describe_item, path, is_file): path
                for path, is_file in file_jobs
            }
            for future in as_completed(futures):
                doc = future.result()
                if doc:
                    docs.append(doc)
                pbar.update(1)
    return docs
