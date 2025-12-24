
from docling.document_converter import DocumentConverter


def load_and_chunk_pdf(pdf_path: str, chunk_size: int = 300):
    """
    Fixed 300-word chunks are enough for demo:
    - Preserves semantic meaning
    - Fast embedding & retrieval
    - Minimal vector count
    """

    converter = DocumentConverter()
    result = converter.convert(pdf_path)

    text = result.document.export_to_text().strip()
    if not text:
        raise ValueError("Empty PDF")

    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size]))

    if not chunks:
        raise ValueError("No chunks returned")

    return chunks
