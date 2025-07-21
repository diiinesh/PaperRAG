import faiss
import numpy as np

def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings) # type: ignore
    return index

def retrieve_top_k(query_embedding, all_chunks, index, k=3):
    if query_embedding is None or len(query_embedding) == 0:
        return []
    
    _, indices = index.search(query_embedding, k)
    return [all_chunks[i] for i in indices[0]]