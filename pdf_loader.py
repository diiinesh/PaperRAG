import pymupdf as fitz
from pathlib import Path

def load_and_chunk_pdf(path, chunk_size=500, overlap=100):
    doc = fitz.open(path)
    all_text = []
    for page in doc:
        text = page.get_text("text", sort=True) # type: ignore
        all_text.append(text)
    text = "\n".join(all_text)

    tokens = text.split()
    chunks = []
    for i in range(0, len(tokens), chunk_size - overlap):
        chunk = " ".join(tokens[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

def load_pdfs_from_dir(directory: str):
    all_chunks = []
    metadata = []

    for pdf_file in Path(directory).glob("*.pdf"):
        chunks = load_and_chunk_pdf(str(pdf_file))
        all_chunks.extend(chunks)
        metadata.extend([pdf_file.name] * len(chunks))
    return all_chunks, metadata