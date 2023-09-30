from doc_uploader.common.factory import FactoryRegistry

from .protocols import DocumentToDB


class DocToDBAdapters(FactoryRegistry[DocumentToDB]):
    _map = {}
    import_pattern = "services/db_handler/uow/*/handler.py"


def get_uow(name: str, *args, **kwargs):
    adapters = DocToDBAdapters.get(name)
    print(DocToDBAdapters._map)
    if not adapters:
        raise ValueError

    return adapters(*args, **kwargs)
