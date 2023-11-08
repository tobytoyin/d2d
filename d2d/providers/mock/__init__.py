import io


# follows the services.SourceIO interface
class IOCatalog:
    @staticmethod
    def source_io(_: dict):
        return io.StringIO("mock io contents")


# follows the services.SourceTasks interface
class TaskCatalog:
    def summary_task(self, _: dict):
        return {"summary": "hello world"}
