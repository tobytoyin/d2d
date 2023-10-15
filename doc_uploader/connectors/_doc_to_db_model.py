from doc_uploader.contracts.database import GraphDataModel
from doc_uploader.contracts.document import Document


def create_graph_model(document: Document) -> GraphDataModel:
    """consume a Document object and transform into a GraphDataModel

    Args:
        document (Document): _description_
    """
    return GraphDataModel(
        node_type=document.metadata.doc_type,
        uid=document.uid,
        relations=list(document.relations),
        contents=document.content.contents,
        fields=document.metadata.properties,
    )


def create_tabular_model(document: Document):
    ...
