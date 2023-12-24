from sentence_transformers import SentenceTransformer


# follows the services.SourceTasks interface
class TaskCatalog:
    @staticmethod
    def embedding(text: str, sent_delim="\r"):
        model = SentenceTransformer("all-MiniLM-L6-v2")

        sentences = text.split(sent_delim)
        embeddings = model.encode(sentences)

        return {
            "vector": tuple(embeddings.mean(axis=0)),
            "source": "sentence_transformers",
            "model": "all-MiniLM-L6-v2",
        }
