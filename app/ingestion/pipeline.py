from app.config.settings import SOURCE_DIR
from app.ingestion.exclusions import EXCLUDED_FILES
from app.ingestion.loaders import load_file
from app.ingestion.metadata import normalize_metadata


def load_knowledge_documents():
    """Load and normalize only documents intended for the knowledge base."""

    documents = []

    for file_path in sorted(SOURCE_DIR.rglob("*")):
        if not file_path.is_file():
            continue

        if file_path.name in EXCLUDED_FILES:
            continue

        loaded_documents = load_file(file_path)

        documents.extend(
            normalize_metadata(document)
            for document in loaded_documents
        )

    return documents