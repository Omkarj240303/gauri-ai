from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI

from app.retrieval.hybrid_retriever import hybrid_search
from app.chains.grounding import check_grounding
from app.web.web_search import web_search


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


def answer(query, context):
    prompt = f"""
Answer using only the context.

Question:
{query}

Context:
{context}

If the answer is not present, say you don't have enough information.
"""

    return llm.invoke(prompt).content


def run(query):
    results = hybrid_search(query)

    if results:
        context = "\n\n".join(
            r["text"]
            for r in results
        )

        grounding = check_grounding(
            query,
            context
        )

        if grounding.decision == "supported":
            return {
                "status": "answered",
                "grounding": grounding,
                "answer": answer(query, context),
                "sources": [
                    r["meta"].get("source_file")
                    for r in results
                ]
            }

    web_results = web_search(query)

    if not web_results:
        return {
            "status": "unsupported",
            "grounding": None,
            "answer": "I don't have enough information to answer this.",
            "sources": []
        }

    web_context = "\n\n".join(
        r["text"]
        for r in web_results
    )

    grounding = check_grounding(
        query,
        web_context
    )

    if grounding.decision != "supported":
        return {
            "status": "unsupported",
            "grounding": grounding,
            "answer": "I couldn't verify this information.",
            "sources": [
                r["url"]
                for r in web_results
            ]
        }

    return {
        "status": "answered",
        "grounding": grounding,
        "answer": answer(query, web_context),
        "sources": [
            r["url"]
            for r in web_results
        ]
    }


rag_chain = RunnableLambda(run)