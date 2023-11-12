from d2d.contracts.documents import Document

from ._taskspec_handler import (
    components_to_document,
    convert_to_document_component,
    payload_validator,
    run_tasks,
    unpack_source_items,
)


class DocumentComposer:
    def run(self, payload: dict) -> Document:
        spec = payload_validator(payload=payload)
        uid, _ = unpack_source_items(spec)
        tasks_results = run_tasks(spec=spec)
        document_components = map(convert_to_document_component, tasks_results)
        document = components_to_document(uid=uid, components=document_components)
        return document
