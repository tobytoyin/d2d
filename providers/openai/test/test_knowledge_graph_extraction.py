import logging
import os
from typing import Iterable

from .. import TaskCatalog


def test_embedding():
    text = """
    This project underscores the potent combination of Neo4j Vector Index and LangChain’s GraphCypherQAChain to navigate through unstructured data and graph knowledge, respectively, and subsequently use Mistral-7b for generating informed and accurate responses.
By employing Neo4j for retrieving relevant information from both a vector index and a graph database, the system ensures that the generated responses are not only contextually rich but also anchored in validated, real-time knowledge.
The implementation demonstrates a practical application of retrieval-augmented generation, where the synthesized information from diverse data sources is utilized to generate responses that are a harmonious blend of pre-trained knowledge and specific, real-time data, thereby enhancing the accuracy and relevance of the responses to user queries.
    """
    api_key = os.environ.get("OPENAI_KEY")
    emb = TaskCatalog.named_entity_relations(text, api_key=api_key)

    print(emb)
