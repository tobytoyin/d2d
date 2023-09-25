import .neo4j as n4j

class UoWFactory:
    def __init__(self, doc_model) -> None:
        self.doc_model = doc_model

    @property
    def neo4j(self):
        return n4j.Neo4JUoW(model=self.doc_model)
