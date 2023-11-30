from __future__ import annotations

import json

from d2d.contracts import documents as doc

from ..interface import DocumentToDB
from .mixin import GraphDBMixin
from .utils import no_quotes_object


class DocumentToNeo4J(DocumentToDB[doc.Document], GraphDBMixin):
    def update_or_create_document(self, document: doc.Document):
        self.update_or_create_document(document)
        self.update_or_create_relations(document)

    def update_or_create_relations(self, document: doc.Document):
        with self.driver.session() as session:
            _ = session.execute_write(
                _NodeCommonProc.detach_all_relationships, document
            )

            if not document.relations:
                return

            _ = session.execute_write(_NodeCommonProc.create_one_to_many_rels, document)

        self.close_driver()

    def delete_document(self, document: doc.Document):
        match_self = _NodeIdentity.get_self(document)
        del_tx = lambda tx: tx.run(f"MATCH (root {match_self}) DETACH DELETE root")

        with self.driver.session() as session:
            _ = session.execute_write(del_tx)
        self.close_driver()

    def update_or_create_document(self, document: doc.Document):
        with self.driver.session() as session:
            _ = session.execute_write(_NodeIdentity.create_self, document)

        self.close_driver()


class _NodeIdentity:
    @staticmethod
    def node_id(document: doc.Document) -> str:
        return document.uid

    @staticmethod
    def node_label(document: doc.Document) -> str:
        return document.metadata.doc_type.capitalize()

    @staticmethod
    def get_self(document: doc.Document) -> str:
        return no_quotes_object({"uid": document.uid})

    @staticmethod
    def create_self(tx, document: doc.Document):
        match_self = _NodeIdentity.get_self(document)
        json_props = _NodeIdentity.read_json_properties(document)
        query = f"""
        WITH apoc.convert.fromJsonMap(\'{json_props}\') AS props
        MERGE ( n {match_self} )
        SET
            n = props,
            n:{_NodeIdentity.node_label(document)},
            n.lastEdited = timestamp()
        """
        tx.run(query)

    @staticmethod
    def read_json_properties(document: doc.Document) -> str:
        # some key values are specifically not compatiable in neo4j
        metadata = {
            k.replace("-", "_"): v for k, v in document.metadata.properties.items()
        }

        return json.dumps(
            {
                "uid": document.uid,
                **document.content.prefix_model_dump(),
                **metadata,
                **document.embedding.prefix_model_dump(),
            },
            default=str,
        )


class _NodeCommonProc:
    @staticmethod
    def detach_all_relationships(tx, document: doc.Document):
        match_self = no_quotes_object({"uid": document.uid})
        q = f"MATCH (root {match_self})-[r]->() DELETE r"
        tx.run(q)

    @staticmethod
    def create_one_to_many_rels(tx, document: doc.Document):
        match_self = no_quotes_object({"uid": document.uid})
        final_query = f"MATCH (root {match_self})"

        if not document.relations.items:
            return

        for idx, rel in enumerate(document.relations.items):
            # for each related document
            # 1. merge to create/ replace existing node
            # 2. merge to create/ replace existing link

            rel_var = f"target{idx}"
            rel_props = no_quotes_object(rel.properties)
            match_rel = no_quotes_object({"uid": rel.rel_uid})

            create_or_merge_subq = f"""
            MERGE ({rel_var} {match_rel})
            MERGE (root)-[ :{rel.rel_type} {rel_props} ]->({rel_var})
            """
            final_query += create_or_merge_subq

        print(final_query)
        tx.run(final_query)
