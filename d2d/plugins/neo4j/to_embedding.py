from d2d.contracts.documents import Document

from ..interface import DocumentPlugin
from .mixin import GraphDBMixin
from .utils import no_quotes_object


class DocumentToN4JEmbedding(DocumentPlugin, GraphDBMixin):
    def update_or_create_embedding(self, document: Document):
        embedding = no_quotes_object(document.embedding.prefix_model_dump())
        match_self = no_quotes_object({"uid": document.uid})

        new_props = {f"root.{k} = {v}" for k, v in embedding.items()}
        query = f"""
        MERGE (root {match_self}
        SET

        """
        print(query)
        tx = lambda tx: tx.run(query)

        with self.driver.session() as session:
            _ = session.execute_write(tx)
        self.close_driver()
