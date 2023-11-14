# follows the services.SourceIO interface
class SourceCatalog:
    source_text = lambda d: "mock io contents"
    uid_gen = lambda d: "mock-id-000"


def _summary(s: str) -> dict[str, str]:
    return {"content": "hello world"}


# follows the services.SourceTasks interface
class TaskCatalog:
    summary = _summary
