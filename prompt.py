def build_prompt(question, context_chunks):
    context = "\n---\n".join(context_chunks)
    return f"""You are a helpful assistant for answering questions based on scientific papers.\n Context: {context} \nQuestion: {question} \nAnswer:"""