import io


# follows the services.SourceTasks interface
class TaskCatalog:
    def source_io(self, d: dict):
        return io.StringIO("text from dummy")

    def summary_task(self, d: dict):
        return {"summary": "hello world"}
