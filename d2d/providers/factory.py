from . import mock
from .interface import SourceTextTasks

_CATALOG = {
    "mock": mock.TaskCatalog,
}


def get_task_fn(provider_name: str, task_name: str) -> SourceTextTasks.TaskSignature:
    provider = _CATALOG.get(provider_name)
    return getattr(provider, task_name)
