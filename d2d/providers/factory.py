import logging

import d2d.contracts.exceptions as exc
from d2d.contracts.interfaces import ProviderSourceMetaHandlers

from . import mock, obsidian, openai
from .interface import SourceTextTasks, TaskFunction

_CATALOG = {
    "mock": mock.TaskCatalog,
    "obsidian": obsidian.TaskCatalog,
    "openai": openai.TaskCatalog,
}


def get_tasks_provider(provider_name: str) -> type[SourceTextTasks] | None:
    provider = _CATALOG.get(provider_name)

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

_SOURCE_CATALOG = {
    "mock": mock.SourceCatalog,
    "obsidian": obsidian.SourceCatalog,
}


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
    provider = _SOURCE_CATALOG.get(provider_name)

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
