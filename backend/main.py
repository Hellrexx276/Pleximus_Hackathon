from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel


from backend.agent import chat_with_agent


# =========================================================
# APP
# =========================================================

app = FastAPI(
    title="Pleximus AI Agent",
    description="AI agent with tool calling",
)


# =========================================================
# FRONTEND PATH
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

FRONTEND_DIR = BASE_DIR / "frontend"

INDEX_FILE = FRONTEND_DIR / "index.html"


# =========================================================
# REQUEST MODEL
# =========================================================

class ChatRequest(BaseModel):

    message: str


# =========================================================
# FRONTEND
# =========================================================

@app.get("/")
def serve_frontend():

    return FileResponse(INDEX_FILE)


# =========================================================
# CHAT API
# =========================================================

@app.post("/chat")
def chat(request: ChatRequest):

    response = chat_with_agent(
        request.message
    )

    return {
        "response": response
    }