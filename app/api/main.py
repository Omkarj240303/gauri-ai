from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.api.schemas import ChatRequest, ChatResponse
from app.chains.rag_chain import rag_chain


app = FastAPI(
    title="Gauri AI Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    query = request.query.strip()

    if not query:
        raise HTTPException(
            status_code=400,
            detail="Query cannot be empty"
        )

    result = rag_chain.invoke(query)
    grounding = result.get("grounding")

    return ChatResponse(
        status=result.get("status", "unsupported"),
        answer=result.get("answer", ""),
        grounding=grounding.decision if grounding else None,
        reason=grounding.reason if grounding else None,
        sources=list(dict.fromkeys(result.get("sources", [])))
    )