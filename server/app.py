from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(msg: Message):
    reply = f"Bot says: {msg.text[::-1]}"  # Simple reverse echo
    return {"reply": reply}

@app.get("/")
def health():
    return {"status": "running"}
