from flashrank import Ranker, RerankRequest

ranker = Ranker()


def rerank_documents(query, documents, top_k=6):
    passages = [
        {
            "id": str(i),
            "text": d.page_content,
            "meta": d.metadata
        }
        for i, d in enumerate(documents)
    ]

    results = ranker.rerank(
        RerankRequest(
            query=query,
            passages=passages
        )
    )

    return results[:top_k]