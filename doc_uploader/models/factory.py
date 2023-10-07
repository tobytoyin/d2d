from doc_uploader.doc_handlers.interfaces import Document
from doc_uploader.models.datamodels import GraphDataModel


def create_graph_model(document: Document):
    """consume a Document object and transform into a GraphDataModel

    Args:
        document (Document): _description_
    """
    # extract doc_type to be the node type in GraphDataModel
    # metadata = document.metadata.model_dump()
    # node_type = metadata.pop("doc_type")

    return GraphDataModel(
        node_type=document.metadata.doc_type,
        uid=document.uid,
        relations=list(document.relations),
        contents=document.contents,
        fields=document.metadata.properties,
    )


def create_tabular_model(document: Document):
    ...
