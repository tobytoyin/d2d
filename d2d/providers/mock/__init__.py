import io


# follows the services.SourceTasks interface
class TaskCatalog:
    def source_io(self, _: dict):
        return io.StringIO("text from dummy")

    def summary_task(self, _: dict):
        return {"summary": "hello world"}
