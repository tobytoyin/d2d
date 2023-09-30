# common Protocol for factory
import fnmatch
import importlib
from abc import ABC
from functools import cache
from importlib import resources
from typing import Dict, Generic, Protocol, TypeVar

T = TypeVar("T")


class FactoryRegistry(Generic[T]):
    """Container of available build-in `T`s under /adapters/*/adapter.py

    Returns:
        _type_: _description_
    """

    _map: Dict[str, T] = {}
    import_loc: str
    import_name_pattern: str

    @classmethod
    def register(cls, name: str):
        """A register decorator to register Interface object

        Args:
            name (str): the key value for this to be used by the Factory
        """

        def _register_decorator(interface: T):
            cls._map.update({name: interface})
            return interface

        return _register_decorator

    @classmethod
    def get(cls, name: str) -> T:
        cls.register_from_adapters()

        return cls._map.get(name, None)

    @classmethod
    @cache
    def register_from_adapters(cls) -> int:
        """run import once to invoke all the registration of the class"""
        modules = resources.contents(cls.import_loc)  # get all modules under /plugins
        print(f"Found Modules at {modules}")

        for mod in fnmatch.filter(modules, cls.import_name_pattern):
            # for mod in filter(lambda f: f.endswith(cls.import_name), modules):
            importlib.import_module(f"{cls.import_loc}.{mod[:-3]}")

        return len(modules)  # return cached when no diff
