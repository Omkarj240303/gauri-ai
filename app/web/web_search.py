import os
from tavily import TavilyClient


client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def web_search(query, k=5):
    results = client.search(
        query=f"site:gauri.com {query}",
        max_results=k,
        search_depth="advanced"
    )

    return [
        {
            "text": r["content"],
            "url": r["url"],
            "title": r.get("title", "")
        }
        for r in results.get("results", [])
    ]