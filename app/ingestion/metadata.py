from langchain_core.documents import Document

from app.ingestion.document_registry import get_document_metadata


KEEP_METADATA_KEYS = {
    "source_file",
    "file_type",
    "page",
    "slide_number",
    "sheet_name",
}


def normalize_metadata(document: Document) -> Document:
    """Normalize document metadata for the Gauri RAG pipeline."""

    original_metadata = document.metadata

    normalized_metadata = {
        key: value
        for key, value in original_metadata.items()
        if key in KEEP_METADATA_KEYS
    }

    normalized_metadata["knowledge_base"] = "gauri"

    source_file = normalized_metadata.get("source_file")

    if source_file:
        normalized_metadata.update(
            get_document_metadata(
                __import__("pathlib").Path(source_file)
            )
        )

    document.metadata = normalized_metadata

    return document