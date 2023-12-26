from d2d.contracts import documents as doc
import json

from .utils import no_quotes_object


def add_named_entites(tx, document: doc.Document):
    # add named entites nodes
    for entity in document.ner.entities:
        json_props = json.dumps(entity.model_dump())
        match_self = no_quotes_object({"id": entity.id})
        query = f"""
        WITH apoc.convert.fromJsonMap({repr(json_props)}) AS props
        MERGE ( n {match_self} )
        SET
            n = props
            n:{entity.type}
            n.lastEdited = timestamp()
        """
        tx.run(query)


def add_relations(tx, document: doc.Document):
    # add named entities relations links
    for rel in document.ner.relations:
        rel_props = no_quotes_object(rel.properties)
        match_self = no_quotes_object({"id": rel.root})
        match_other = no_quotes_object({"id": rel.target})
        q = f"MERGE (root {match_self})-[ :{rel.type} {rel_props} ]->(other {match_other})"
        tx.run(q)
