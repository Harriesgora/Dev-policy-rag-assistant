from fastapi import FastAPI
from pydantic import BaseModel, Field
from services.question_service import process_question
from services.document_loader import load_documents, chunk_documents
from services.retrieval_service import retrieve_relevant_chunks
from services.llm_service import generate_response
app = FastAPI()

class Question(BaseModel):
    question: str = Field(..., min_length=1,)

@app.get("/")
def read_root():
    return {"message": "api is working"}


@app.post("/ask")
def ask_question(question: Question):

    answer = process_question(question.question)
    return {
        "question": question.question, 
            "answer": answer
            } 

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/documents/chunks")
def get_document_chunks():
    documents = load_documents()
    chunks = chunk_documents(documents)

    return {
        "total chunks": len(chunks),
        "chunks": chunks}

@app.get("/retrieve")
def retrieve_chunks(question: str):
    relevant_chunks = retrieve_relevant_chunks(question)

    return {
        "question": question,
        "relevant_chunks": relevant_chunks
    }

@app.get("/ask-rag")
def ask_question_rag(question: str):
    retrieved_chunks = retrieve_relevant_chunks(question)
    answer = generate_response(question, retrieved_chunks)

    return {
        "question": question,
        "answer": answer,
        "sources": retrieved_chunks
    }