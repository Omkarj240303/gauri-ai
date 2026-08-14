from app.ingestion.pipeline import load_knowledge_documents
from app.ingestion.chunking import chunk_documents
from app.retrieval.vectorstore import create_vectorstore
from app.retrieval.bm25_retriever import build_bm25, search_bm25
from app.retrieval.reranker import rerank_documents
from app.retrieval.query_rewriter import rewrite_query

VECTOR_K = 6
BM25_K = 4
FINAL_K = 6

documents = load_knowledge_documents()
chunks = chunk_documents(documents)

vectorstore = create_vectorstore(chunks)
bm25 = build_bm25(chunks)


def _key(document):
    return (
        document.metadata.get("source_file"),
        document.metadata.get("page"),
        document.metadata.get("slide_number"),
        document.page_content
    )

def hybrid_search(query):
    rewritten = rewrite_query(query)

    queries = [query]

    if rewritten and rewritten.lower() != query.lower():
        queries.append(rewritten)

    vector_results = []
    bm25_results = []

    for q in queries:
        try:
            vector_results += vectorstore.similarity_search(
                q,
                k=VECTOR_K
            )
        except Exception:
            pass

        try:
            bm25_results += [
                d
                for d, _ in search_bm25(
                    bm25,
                    chunks,
                    q,
                    BM25_K
                )
            ]
        except Exception:
            pass

    results = []
    seen = set()

    for document in vector_results + bm25_results:
        key = (
            document.metadata.get("source_file"),
            document.metadata.get("page"),
            document.page_content
        )

        if key not in seen:
            seen.add(key)
            results.append(document)

    if not results:
        return []

    return rerank_documents(
        query,
        results,
        FINAL_K
    )