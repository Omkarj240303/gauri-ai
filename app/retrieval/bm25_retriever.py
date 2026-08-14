from rank_bm25 import BM25Okapi


def build_bm25(documents):
    tokens = [d.page_content.lower().split() for d in documents]
    return BM25Okapi(tokens)


def search_bm25(bm25, documents, query, k=4):
    scores = bm25.get_scores(query.lower().split())
    indexes = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )[:k]

    return [(documents[i], scores[i]) for i in indexes]