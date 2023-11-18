import asyncio

import d2d.contracts.documents as doc

from .mixin import GraphDBMixin
from .utils import no_quotes_object


class NodeIdentity:
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
        match_self = NodeIdentity.get_self(document)
        print(match_self)
        query = f"""
        MERGE ( n {match_self} )
        SET
            n:{NodeIdentity.node_label(document)},
            n.lastEdited = timestamp()
        """
        print("------------")
        print(query)
        tx.run(query)


class NodeCommonProc:
    @staticmethod
    def detach_all_relationships(tx, document: doc.Document):
        match_self = no_quotes_object({"uid": document.uid})
        q = f"MATCH (root {match_self})-[r]->() DELETE r"
        tx.run(q)

    @staticmethod
    def create_one_to_many_rels(tx, document: doc.Document):
        match_self = no_quotes_object({"uid": document.uid})
        final_query = f"MATCH (root {match_self})"

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
