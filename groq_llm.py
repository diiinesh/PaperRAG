import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override=True)

from pathlib import Path
from langchain_groq import ChatGroq
from pydantic import SecretStr

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment!")

llm = ChatGroq(
    api_key=SecretStr(api_key),
    model="llama3-70b-8192",  # or llama-3.1-8b-instant if you prefer
    temperature=0.3,
    max_retries=2
)

chat_history = []

def query_llm_with_history(user_input, retrieved_chunks):
    context = "\n---\n".join(retrieved_chunks)
    system_prompt = (
        "You are a helpful assistant that answers questions about scientific papers using the context provided."
    )
    full_prompt = f"{system_prompt}\n\nContext:\n{context}"

    chat_history.append({"role": "user", "content": user_input})

    full_messages = [{"role": "system", "content": full_prompt}] + chat_history

    response = llm.invoke(full_messages)

    chat_history.append({"role": "assistant", "content": response.content})

    return response.content
