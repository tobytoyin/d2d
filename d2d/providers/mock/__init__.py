# follows the services.SourceIO interface
class IOCatalog:
    source_text = lambda d: "mock io contents"
    uid_gen = lambda d: "mock-id-000"


# follows the services.SourceTasks interface
class TaskCatalog:
    summary = lambda s: {"content": "hello world"}
