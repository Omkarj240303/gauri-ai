from pydantic import BaseModel


class ChatRequest(BaseModel):
    query: str


class ChatResponse(BaseModel):
    status: str
    answer: str
    grounding: str | None = None
    reason: str | None = None
    sources: list[str] = []