from fastapi import FastAPI
from pydantic import BaseModel
from app.chat import generate_response

app = FastAPI(title="🦆 Rubber Duckie - AI Debugging Companion")

class ChatRequest(BaseModel):
    user_id: str
    message: str


class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = generate_response(request.user_id, request.message)
    return ChatResponse(response=answer)


