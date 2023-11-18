# follows the services.SourceIO interface
class SourceCatalog:
    @staticmethod
    def source_text(d: dict):
        print(f"source_text - receive {d}")
        print(f"source_text - read from {d['path']}")
        return "mock io contents"

    uid_gen = lambda d: "mock-id-000"


from ..interface import SourceTextTasks


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
        }

    @staticmethod
    def relations(text):
        rel1 = {
            "rel_uid": "0000",
            "rel_type": "link",
        }
        rel2 = {
            "rel_uid": "0001",
            "rel_type": "link",
            "properties": {"key1": "value1"},
        }
        return {"items": [rel1, rel2]}
