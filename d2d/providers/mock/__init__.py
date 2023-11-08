import io


# follows the services.SourceIO interface
class IOCatalog:
    source_io = lambda d: io.StringIO("mock io contents")


# follows the services.SourceTasks interface
class TaskCatalog:
    summary_task = lambda s: {"summary": "hello world"}
