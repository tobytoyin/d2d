from doc_uploader.common.factory import FactoryRegistry

from .protocols import DocumentToDB


class DocToDBAdapters(FactoryRegistry[DocumentToDB]):
    import_loc = "doc_uploader.services.uploader.uow"
    import_name_pattern = "handler.py"


def get_uow(name: str, *args, **kwargs):
    adapters = DocToDBAdapters.get(name)
    if not adapters:
        raise ValueError

    return adapters(*args, **kwargs)
