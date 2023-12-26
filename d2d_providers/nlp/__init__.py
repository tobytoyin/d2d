from sentence_transformers import SentenceTransformer


# follows the services.SourceTasks interface
class TaskCatalog:
    @staticmethod
    def embedding(text: str, sent_delim="\r"):
        return
        # model = SentenceTransformer("all-MiniLM-L6-v2")

        # sentences = text.split(sent_delim)
        # embeddings = model.encode(sentences)
        # doc_emb = list(embeddings.mean(axis=0))

        # return {
        #     "vector": doc_emb,
        #     "source": "sentence_transformers",
        #     "model": "all-MiniLM-L6-v2",
        #     "dimension": len(doc_emb),
        # }
