from rank_bm25 import BM25Okapi


def tokenize(text: str) -> list[str]:
    """Tokenize text for BM25 retrieval."""
    return text.lower().split()


def build_bm25(documents):
    """Build a BM25 index from documents."""

    tokenized_documents = [
        tokenize(document.page_content)
        for document in documents
    ]

    return BM25Okapi(tokenized_documents)


def search_bm25(
    bm25,
    documents,
    query: str,
    k: int = 2,
):
    """Return top BM25 documents with scores."""

    query_tokens = tokenize(query)

    scores = bm25.get_scores(query_tokens)

    ranked_indices = sorted(
        range(len(scores)),
        key=lambda index: scores[index],
        reverse=True,
    )[:k]

    return [
        (documents[index], scores[index])
        for index in ranked_indices
    ]