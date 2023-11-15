# follows the services.SourceIO interface
class SourceCatalog:
    @staticmethod
    def source_text(d: dict):
        print(f"receive {d}")
        print(f"read from {d['path']}")
        return "mock io contents"

    uid_gen = lambda d: "mock-id-000"


def _summary(_: str) -> dict[str, str]:
    return {"content": "hello world"}


# follows the services.SourceTasks interface
class TaskCatalog:
    summary = _summary
