import logging

from . import mock
from .interface import SourceTextTasks, TaskFunction

_CATALOG = {
    "mock": mock.TaskCatalog,
}


def get_task_fn(provider_name: str, task_name: str) -> TaskFunction | None:
    try:
        provider = _CATALOG.get(provider_name)
        return getattr(provider, task_name)

    except AttributeError:
        logging.warning(
            "'%s' does not exist in '%s' provider",
            task_name,
            provider_name,
        )
        return None
