from .mock import MockUoW
from .neo4j import Neo4JUoW


class UoWFactory:
    def __init__(self, doc_model) -> None:
        self.doc_model = doc_model

    @property
    def mock(self):
        return MockUoW(model=self.doc_model)

    @property
    def neo4j(self):
        return Neo4JUoW(model=self.doc_model)
