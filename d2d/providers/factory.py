import importlib
import logging
from functools import cache
from typing import Any, Literal

import d2d.contracts.exceptions as exc
from d2d.configs import Config
from d2d.contracts.interfaces import ProviderSourceMetaHandlers

from .interface import SourceTextTasks, TaskFunction


class ProvidersRegistry:
    # Herein we register different providers based on the keyvalue map provided
    # by configs.providers
    providers = Config.get_providers()
    catalog = {}

    @classmethod
    def add_provider(cls, provider_name, path) -> None:
        # add provider during runtime
        module = importlib.import_module(path.replace("/", "."))
        cls.catalog[provider_name] = module
        logging.debug("%s from '%s' is loaded", provider_name, path)

    @classmethod
    @cache
    def import_providers(cls) -> None:
        for provider_name, path in cls.providers.items():
            cls.add_provider(provider_name, path)

    @classmethod
    def view_providers(cls) -> None:
        logging.info(cls.catalog)

    @classmethod
    def get_catalog(cls, type_name: Literal["TaskCatalog", "SourceCatalog"]) -> dict:
        _catalog = {}
        for key, module in cls.catalog.items():
            try:
                _catalog[key] = getattr(module, type_name)
            except AttributeError:
                continue
        return _catalog


# init import
ProvidersRegistry.import_providers()


### Factory functions ###
def get_tasks_provider(provider_name: str) -> type[SourceTextTasks] | None:
    provider = ProvidersRegistry.get_catalog("TaskCatalog").get(provider_name)

    if provider is None:
        logging.warning("provider '%s' does not exist", provider_name)
        return

    return provider  # type: ignore


def get_task_fn(provider_name: str, task_name: str) -> TaskFunction | None:
    try:
        provider = get_tasks_provider(provider_name=provider_name)
        return getattr(provider, task_name)

    except AttributeError:
        logging.warning(
            "'%s' does not exist in '%s' provider",
            task_name,
            provider_name,
        )
        return None


###### Source Catalog ######
# This is functions where the Providers provides some functionality which
# would interact with 3rd party data source
def get_source_handling_provider(
    provider_name: str,
) -> type[ProviderSourceMetaHandlers]:
    """Retrieve the selected provider to interact with source

    :param provider_name: _description_
    :type provider_name: str
    :raises TypeError: when provider
    :raises TypeError: _description_
    :return: _description_
    :rtype: type[ProviderSourceMetaHandlers]
    """
    provider = ProvidersRegistry.get_catalog("SourceCatalog").get(provider_name)

    if provider is None:
        logging.warning("provider '%s' does not exist", provider_name)
        raise exc.ProviderNotFound

    # ensure interface
    if not issubclass(provider, ProviderSourceMetaHandlers):
        logging.warning(
            "provider '%s' has implemented incorrect interface",
            provider_name,
        )
        raise exc.ProviderNotFound

    return provider
