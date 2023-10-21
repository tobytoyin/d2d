# common Protocol for factory
import glob
import importlib
from functools import cache
from typing import Dict, Generic, Protocol, TypeVar

T = TypeVar("T", contravariant=True)


class FactoryRegistry(Generic[T]):
    """Container of available build-in `T`s under /adapters/*/adapter.py

    Returns:
        _type_: _description_
    """

    _map: Dict[str, T] = {}
    import_pattern: str

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
        import d2d

        # since this will be installed at python/libs as root directory
        # it needs to find the other modules relative to this root
        root_module = d2d.__path__[0]
        found_modules = glob.glob(cls.import_pattern, root_dir=root_module)
        print("Found: ", found_modules)

        for path in found_modules:
            # create the in-module package path
            module_name = f"{d2d.__name__}/{path}"
            module_name = module_name.replace("/", ".")
            module_name = module_name.replace(".py", "")
            print(module_name)

            importlib.import_module(module_name)

            print(f"Registered {module_name}")

        return len(found_modules)  # return cached when no diff
