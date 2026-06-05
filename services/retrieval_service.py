from services.embedding_service import generate_embedding
from services.document_loader import load_documents, chunk_documents
from sklearn.metrics.pairwise import cosine_similarity  

def retrieve_relevant_chunks(question, top_k=3):
    documents = load_documents()
    chunks = chunk_documents(documents)

    question_embedding = generate_embedding(question)

    scored_chunks = []

    for chunk in chunks:
        similarity_score = cosine_similarity(
            [question_embedding],
            [chunk["embedding"]]
        )[0][0]

        scored_chunks.append({
            "document_name": chunk["document_name"],
            "chunk_id": chunk["chunk_id"],
            "chunk_text": chunk["chunk_text"],
            "similarity_score": float (similarity_score)
        })


    scored_chunks.sort(key=lambda chunk: chunk["similarity_score"], reverse=True)

    return scored_chunks[:top_k]