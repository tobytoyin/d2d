import json

from d2d.contracts import documents as doc

from .utils import no_quotes_object


def add_named_entites(tx, document: doc.Document):
    if document.ner.entities is None: 
        return 
    
    # add named entites nodes
    for entity in document.ner.entities:
        json_props = json.dumps({"id": entity.id, **entity.properties}, default=str)
        match_root = no_quotes_object({"id": entity.id})
        match_doc = no_quotes_object({"uid": document.uid})
        query = f"""
        WITH apoc.convert.fromJsonMap({repr(json_props)}) AS props
        MERGE ( n {match_root} )
        MERGE (doc {match_doc})
        SET
            n = props,
            n:NERNode:{entity.type},
            n.lastEdited = timestamp()

        MERGE (doc)-[ :NERContain ]->(n)
        """
        print(query)
        tx.run(query)


def add_relations(tx, document: doc.Document):
    if document.ner.relations is None: 
        return 
    
    # add named entities relations links
    for rel in document.ner.relations:
        rel_props = no_quotes_object(rel.properties)
        match_root = no_quotes_object({"id": rel.root})
        match_other = no_quotes_object({"id": rel.target})
        q = f"""
        MATCH (root {match_root})
        MATCH (other {match_other})
        MERGE (root)-[ :{rel.type} {rel_props} ]->(other)
        """
        tx.run(q)
