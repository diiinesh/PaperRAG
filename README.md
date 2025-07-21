# PaperRAG – Retrieval-Augmented Generation for Scientific Papers

PaperRAG is a lightweight, modular Retrieval-Augmented Generation (RAG) system designed for question-answering over scientific documents. The system uses FAISS for semantic retrieval and Groq-hosted LLaMA-3 for generating grounded, context-aware responses. It supports multi-document processing, page-level source attribution, and multi-turn chat interactions.

---

## Features

- Load and process multiple scientific papers (PDF format)
- Chunk documents by page with contextual overlap
- Generate embeddings using `sentence-transformers`
- Perform semantic similarity search using FAISS
- Retrieve top-k relevant chunks and pass them to an LLM
- Generate answers using Groq-hosted LLaMA-3
- Return the document name and page number for each supporting chunk
- Maintain multi-turn chat memory across user queries

---

## Getting Started

### 1. Clone the Repository then call

```bash
cd paper-rag
python main.py
