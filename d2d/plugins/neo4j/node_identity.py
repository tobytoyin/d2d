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
