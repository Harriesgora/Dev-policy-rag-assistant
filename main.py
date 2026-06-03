from fastapi import FastAPI
from pydantic import BaseModel, Field
from services.question_service import process_question
from services.document_loader import load_documents, chunk_documents
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