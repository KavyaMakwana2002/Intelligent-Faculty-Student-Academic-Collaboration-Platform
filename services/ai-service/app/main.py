from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="EduConnect AI Service")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the EduConnect AI Service!"}

@app.post("/chat")
def chat(request: ChatRequest):
    # Basic mock AI logic
    return {"reply": f"AI says: I received your message '{request.message}'"}
