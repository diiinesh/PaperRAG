from pdf_loader import load_and_chunk_pdf, load_pdfs_from_dir
from embedder import embed_chunks, embed_query
from retriever import build_faiss_index, retrieve_top_k
from groq_llm import query_llm_with_history


all_chunks = load_pdfs_from_dir("papers/")
texts = [chunk["content"] for chunk in all_chunks]
embeddings = embed_chunks(texts)
index = build_faiss_index(embeddings)

print("Loaded papers. Ask question. Type 'exit' to quit\n")

while True:
    question = input("You: ")
    if question.lower().strip() == "exit":
        break

    query_vec = embed_query(question)
    print(f"Query shape: {query_vec.shape}")  # should be (1, 384)

    top_chunks = retrieve_top_k(query_vec, all_chunks, index, k=3)

    print("\n Retrieved from: ")
    for chunk in top_chunks:
        print(f"- {chunk['source']} (page {chunk['page']})")
    
    answer = query_llm_with_history(question, [chunk['content'] for chunk in top_chunks])
    print("\n Assistant:\n" + str(answer) + "\n") # type: ignore