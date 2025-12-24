from moderation.moderator import moderate_text
from llm.gpt5_nano import mock_gpt5_nano
from utils.retry import retry
from rag.loader import load_and_chunk_pdf
from rag.vector_store import VectorStore
from rag.retriever import retrieve


def main():
    pdf_path = "data/sample.pdf"
    query = "What is this document about?"

    try:
        chunks = load_and_chunk_pdf(pdf_path)

        store = VectorStore()
        store.build(chunks)

        rag_result = retrieve(store, query)

        moderation = moderate_text(query)
        if not moderation["allowed"]:
            print(moderation)
            return

        response = retry(lambda: mock_gpt5_nano(query), retries=1)
        print(response)

    except Exception as e:
        print("[ERROR]", e)


if __name__ == "__main__":
    main()
