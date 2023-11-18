# follows the services.SourceIO interface
from .processor import links_processor


class SourceCatalog:
    @staticmethod
    def source_text(d: dict):
        with open(d["path"], "r") as f:
            return f.read()

    @staticmethod
    def uid_gen(d):
        return str(d["path"]).split("/")[-1].split(".")[0]


# follows the services.SourceTasks interface
class TaskCatalog:
    @staticmethod
    def summary(text):
        return {
            "content": "hello world",
        }

    @staticmethod
    def metadata(text):
        return {
            "doc_type": "mock",
            "properties": {"type": "mock"},
        }

    @staticmethod
    def relations(text):
        return links_processor(text)
