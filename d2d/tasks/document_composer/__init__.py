from d2d.contracts.documents import Document

from ._source_handler import get_source_contents, payload_handler

# from ._task_handler import get_task_fn


class DocumentComposer:
    def run(self, payload: dict):
        spec = payload_handler(payload=payload)
