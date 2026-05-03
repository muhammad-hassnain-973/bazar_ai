import numpy as np


_embedding_model = None


def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        try:
            from fastembed import TextEmbedding
            _embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
        except Exception as e:
            return None
    return _embedding_model


def embed_texts(texts):
    model = get_embedding_model()
    if model is None or not texts:
        return np.zeros((len(texts), 384), dtype="float32")
    try:
        embeddings = list(model.embed(texts))
        return np.array(embeddings, dtype="float32")
    except Exception:
        return np.zeros((len(texts), 384), dtype="float32")


def build_faiss_index(chunks):
    import faiss
    if not chunks:
        return None, []
    embeddings = embed_texts(chunks)
    if embeddings is None or embeddings.shape[0] == 0:
        return None, chunks
    dim = embeddings.shape[1]
    faiss.normalize_L2(embeddings)
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)
    return index, chunks


def semantic_search(query, index, chunks, k=5):
    if index is None or not chunks:
        return chunks[:k] if chunks else []
    try:
        import faiss
        q_emb = embed_texts([query])
        faiss.normalize_L2(q_emb)
        distances, indices = index.search(q_emb, min(k, len(chunks)))
        results = []
        for idx in indices[0]:
            if 0 <= idx < len(chunks):
                results.append(chunks[idx])
        return results
    except Exception:
        return chunks[:k]
