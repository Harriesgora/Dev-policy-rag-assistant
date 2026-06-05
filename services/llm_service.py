import ollama


def generate_response(question, retrieved_chunks):
    context = "\n\n".join(
        [chunk["chunk_text"] for chunk in retrieved_chunks]
    )

    prompt = f"""
You are an internal developer policy assistant.

Answer the user's question using ONLY the provided context.

Question:
{question}

Context:
{context}
"""

    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]