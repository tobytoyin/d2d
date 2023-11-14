import logging

from . import mock
from .interface import SourceTextTasks, TaskFunction

_CATALOG = {
    "mock": mock.TaskCatalog,
}


def get_provider(provider_name: str) -> type[SourceTextTasks] | None:
    provider = _CATALOG.get(provider_name)

    if provider is None:
        logging.warning(
            "'%s' does not exist",
            provider_name,
        )
    return provider  # type: ignore


def get_task_fn(provider_name: str, task_name: str) -> TaskFunction | None:
    try:
        provider = get_provider(provider_name=provider_name)
        return getattr(provider, task_name)

    except AttributeError:
        logging.warning(
            "'%s' does not exist in '%s' provider",
            task_name,
            provider_name,
        )
        return None
