from d2d.contracts import documents as doc

from .utils import no_quotes_object


def add_named_entites(tx, document: doc.Document):
    # add named entites nodes
    for entity in document.ner.entites:
        json_props = entity.model_dump(mode="json")
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
