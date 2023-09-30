import importlib
import logging
from functools import cache
from importlib import resources
from typing import Dict

from .interfaces import Document, DocumentAdapter, DocumentProps

ADAPTERS_LOC = "doc_uploader.doc_handlers.adapters"
ADAPTERS_PYNAME = "adapter.py"


class Registry:
    registry: Dict[str, DocumentAdapter] = {
        # factory_key: <__class__ object>
    }

    @classmethod
    def register(cls, name: str):
        """A register decorator to register Interface object

        Args:
            name (str): the key value for this to be used by the Factory
        """

        def _register_decorator(interface: DocumentAdapter):
            logging.debug(f"registered: {interface} with {name}")
            cls.registry.update({name: interface})
            return interface

        return _register_decorator

    @classmethod
    def get_interface(cls, name: str):
        return cls.registry.get(name, None)


# factory function
@cache
def register_from_adapters():
    """run import once to invoke all the registration of the class"""
    modules = resources.contents(ADAPTERS_LOC)  # get all modules under /plugins
    print(f"Found Modules at {modules}")

    for mod in filter(lambda f: f.endswith(ADAPTERS_PYNAME), modules):
        print(mod)
        importlib.import_module(f"{ADAPTERS_LOC}.{mod[:-3]}")


def get_adapter(name: str, *args, **kwargs):
    register_from_adapters()  # invoke all registration
    adapters = Registry.get_interface(name)
    if not adapters:
        raise ValueError

    return adapters(*args, **kwargs)


def get_props(adapter_name: str, *args, **kwargs):
    adapter = get_adapter(name=adapter_name, *args, **kwargs)
    return DocumentProps(adapter)


def get_document(adapter_name: str, *args, **kwargs):
    props = get_props(adapter_name=adapter_name, *args, **kwargs)

    # use the prop to return as a document
    doc = Document(
        uid=props.id,
        contents=props.contents,
        metadata=props.metadata,
        relations=props.relations,
    )
    return doc
