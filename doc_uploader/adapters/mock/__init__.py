# define the protocols and source types in this file here for registration
class SourceHandlers:
    SOURCE_READER = lambda s: "duumy content"
    LINK_PROCESSOR = lambda: "dummy link"
    META_PROCESSOR = lambda: {"doc_type": "dummy"}
