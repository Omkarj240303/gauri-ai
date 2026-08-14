from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


def rewrite_query(query):
    prompt = f"""
Rewrite this query for search.

Keep the exact meaning.
Keep the important nouns and technologies.
Do not add facts.
Return only a short search query.

Query:
{query}
"""

    return llm.invoke(prompt).content.strip()