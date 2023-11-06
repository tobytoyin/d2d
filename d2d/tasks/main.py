from providers.mock import TaskCatalog

from d2d.contracts.services import SourceTasks


def get_provider(name: str) -> type[SourceTasks]:
    provider_catalog = {
        "mock": TaskCatalog,
    }.get(name, None)

    if not provider_catalog:
        raise ValueError

    return provider_catalog
