from doc_uploader.common.factory import FactoryRegistry

from .uow.mock.handler import MockUoW
from .uow.neo4j.handler import Neo4JUoW


class DocToDBAdapters(FactoryRegistry):
    import_loc = "doc_uploader.services.uploader.uow"
    import_name = "handler.py"


def get_uow(name: str, *args, **kwargs):
    adapters = DocToDBAdapters.get_interface(name)
    if not adapters:
        raise ValueError

    return adapters(*args, **kwargs)
