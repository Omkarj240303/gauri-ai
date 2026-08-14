from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


CHUNK_SIZE = 1200
CHUNK_OVERLAP = 150


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    separators=[
        "\n\n",
        "\n",
        ". ",
        " ",
        "",
    ],
)


def chunk_documents(documents: list[Document]) -> list[Document]:
    """Create retrieval chunks while preserving source metadata."""

    chunks = []

    for document in documents:
        file_type = document.metadata.get("file_type")

        # PPTX: one slide is already a semantic unit.
        if file_type == "pptx":
            chunks.append(document)
            continue

        # XLSX: preserve each sheet as a structured unit for now.
        if file_type == "xlsx":
            chunks.append(document)
            continue

        # PDF and TXT: split larger text documents.
        split_documents = text_splitter.split_documents(
            [document]
        )

        chunks.extend(split_documents)

    return chunks
