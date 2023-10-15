import numpy as np
from sentence_transformers import SentenceTransformer


def parse_sentences(doc: str):
    return doc.split('.')


class MockEmbedding:
    model = SentenceTransformer('all-MiniLM-L6-v2')

    def __init__(self, doc) -> None:
        self.doc = doc

    @property
    def doc_embeddings(self):
        sentences = parse_sentences(self.doc)
        embeddings = self.model.encode(sentences)
        emb = np.mean(embeddings, axis=0)
        return np.zeros(shape=emb.shape)


class SentenceEmbedding:
    model = SentenceTransformer('all-MiniLM-L6-v2')

    def __init__(self, doc) -> None:
        self.doc = doc

    @property
    def doc_embeddings(self):
        sentences = parse_sentences(self.doc)
        embeddings = self.model.encode(sentences)
        return np.mean(embeddings, axis=0)
