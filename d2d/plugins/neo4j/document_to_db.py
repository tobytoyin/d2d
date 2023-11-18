from d2d.contracts.documents import Document

from ..interface import DocumentToDB
from .identity_checks import NodeCommonProc, NodeIdentity
from .mixin import GraphDBMixin


class DocumentToNeo4J(DocumentToDB[Document], GraphDBMixin):
    def update_or_create_relations(self, document: Document):
        with self.driver.session() as session:
            _ = session.execute_write(NodeCommonProc.detach_all_relationships, document)

            if not document.relations:
                return

            _ = session.execute_write(NodeCommonProc.create_one_to_many_rels, document)

        self.close_driver()

    def delete_document(self, document: Document):
        match_self = NodeIdentity.get_self(document)
        del_tx = lambda tx: tx.run(f"MATCH (root {match_self}) DETACH DELETE root")

        with self.driver.session() as session:
            _ = session.execute_write(del_tx)
        self.close_driver()

    def update_or_create_document(self, document: Document):
        with self.driver.session() as session:
            _ = session.execute_write(NodeIdentity.create_self, document)

        self.close_driver()
