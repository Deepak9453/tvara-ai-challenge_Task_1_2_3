import faiss
from sentence_transformers import SentenceTransformer


class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer("intfloat/e5-small-v2")
        self.index = None
        self.chunks = []

    def build(self, chunks):
        embeddings = self.model.encode(chunks, convert_to_numpy=True)
        dim = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)
        self.chunks = chunks

    def search(self, query, top_k=3):
        if not query.strip():
            raise ValueError("Query is empty")

        query_embedding = self.model.encode([query], convert_to_numpy=True)
        scores, indices = self.index.search(query_embedding, top_k)

        return {
            "chunks": [self.chunks[i] for i in indices[0]],
            "scores": [float(s) for s in scores[0]],
        }
