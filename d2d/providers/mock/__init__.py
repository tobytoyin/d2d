# follows the services.SourceIO interface
class IOCatalog:
    source_text = lambda d: "mock io contents"


# follows the services.SourceTasks interface
class TaskCatalog:
    summary_task = lambda s: {"summary": "hello world"}
