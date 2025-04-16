import os
import pandas as pd
import pdfplumber

SUPPORTED_TYPES = ["pdf", "csv", "xlsx", "txt"]

def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower().strip(".")
    if ext not in SUPPORTED_TYPES:
        raise ValueError(f"Unsupported file type: {ext}")

    if ext == "pdf":
        with pdfplumber.open(file_path) as pdf:
            text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
        return text, "PDF"

    elif ext == "csv":
        df = pd.read_csv(file_path)
        return df.to_string(index=False), "CSV"

    elif ext == "xlsx":
        df = pd.read_excel(file_path)
        return df.to_string(index=False), "Excel"

    elif ext == "txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read(), "Text"

    return "", "Unknown"
