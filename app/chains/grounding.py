from pydantic import BaseModel
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


class GroundingResult(BaseModel):
    decision: str
    reason: str


def check_grounding(query, context):
    prompt = f"""
Question:
{query}

Context:
{context}

Decide whether the context supports answering the question.

Return JSON:
{{
  "decision": "supported" or "unsupported",
  "reason": "short explanation"
}}
"""

    result = llm.with_structured_output(
        GroundingResult
    ).invoke(prompt)

    return result