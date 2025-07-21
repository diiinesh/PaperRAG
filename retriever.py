import faiss
import numpy as np

def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings) # type: ignore
    return index

def retrieve_top_k(query_embedding, chunk_texts, index, k=3):
    if query_embedding is None or len(query_embedding) == 0:
        return []
    
    _, indices = index.search(query_embedding, k)
    return [chunk_texts[i] for i in indices[0]]