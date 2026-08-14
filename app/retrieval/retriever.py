from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from app.config.settings import CHROMA_DIR
from app.retrieval.vectorstore import (
    COLLECTION_NAME,
    EMBEDDING_MODEL,
)


def get_vectorstore() -> Chroma:
    """Load the persisted Gauri Chroma collection."""

    embeddings = OpenAIEmbeddings(
        model=EMBEDDING_MODEL
    )

    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(CHROMA_DIR),
    )


def get_retriever(k: int = 10):
    """Return the baseline Gauri retriever."""

    vectorstore = get_vectorstore()

    return vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k},
    )


def search_with_scores(query: str, k: int = 10):
    """Return internal documents with Chroma relevance scores."""

    vectorstore = get_vectorstore()

    return vectorstore.similarity_search_with_relevance_scores(
        query,
        k=k,
    )