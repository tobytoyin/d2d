# follows the services.SourceIO interface
class SourceCatalog:
    @staticmethod
    def source_text(d: dict):
        print(f"receive {d}")
        print(f"read from {d['path']}")
        return "mock io contents"

    uid_gen = lambda d: "mock-id-000"


from ..interface import SourceTextTasks


# follows the services.SourceTasks interface
class TaskCatalog:
    @staticmethod
    def summary(text: int) -> dict[str, str]:
        return {"content": "hello world"}
