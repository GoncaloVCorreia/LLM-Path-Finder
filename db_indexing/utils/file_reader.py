import fitz  # PyMuPDF
from docx import Document as DocxDocument

def read_docx_text(path, max_chars=30000):

    #Extracts text from a DOCX (Microsoft Word) file using python-docx.
    #Limits output to max_chars to avoid excessive memory use.

    try:
        doc = DocxDocument(path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text[:max_chars]
    except Exception as e:
        print(f"[!] Error reading DOCX {path}: {e}")
        return ""

def read_pdf_text(path, max_chars=30000) :
    """
    Extracts text from a PDF file using PyMuPDF (fitz).
    Limits output to max_chars to avoid excessive memory use.
    """
    try:
        text = ""
        with fitz.open(path) as doc:
            for page in doc:
                text += page.get_text()
                if len(text) >= max_chars:
                    break
        return text[:max_chars]
    except Exception as e:
        print(f"[!] Error reading PDF {path}: {e}")
        return ""

def read_file_content(path, max_chars= 30000):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read(max_chars)
    except:
        return ""
