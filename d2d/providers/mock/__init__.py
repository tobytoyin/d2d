# follows the services.SourceIO interface
class IOCatalog:
    source_text = lambda d: "mock io contents"


# follows the services.SourceTasks interface
class TaskCatalog:
    summary = lambda s: {"content": "hello world"}
