from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "api is working"}

@app.get("/ask")
def ask_question(question: str):
    return {"question": question, "response": "This is a placeholder answer."} 