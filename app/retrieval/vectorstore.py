import os

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


def create_vectorstore(documents):
    embeddings = OpenAIEmbeddings(
        model=os.getenv(
            "EMBEDDING_MODEL",
            "text-embedding-3-small"
        )
    )

    return Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory="storage/chroma",
        collection_name="gauri"
    )