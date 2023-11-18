from d2d.contracts.documents import Document

from ..interface import DocumentToDB
from .identity_checks import NodeCommonProc, NodeIdentity
from .mixin import GraphDBMixin


class DocumentToNeo4J(DocumentToDB[Document], GraphDBMixin):
    def update_or_create_relations(self, document: Document):
        with self.get_driver().session() as session:
            _ = session.execute_write(NodeCommonProc.detach_all_relationships, document)

            if not document.relations:
                return

            _ = session.execute_write(NodeCommonProc.create_one_to_many_rels, document)

    def delete_document(self, document: Document):
        return

    def update_or_create_document(self, document: Document):
        with self.get_driver().session() as session:
            _ = session.execute_write(NodeIdentity.create_self, document)
