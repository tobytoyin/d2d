import asyncio
from typing import Iterable

from d2d.contracts.documents import Document, DocumentComponent
from d2d.contracts.enums import TaskKeyword
from d2d.contracts.payload import Source, SourceSpec, TaskSpec

from ._source_handler import get_source_contents, payload_handler
from ._task_handler import task_handler


class DocumentComposer:
    def run(self, payload: dict):
        spec = payload_handler(payload=payload)

        sources = spec.sources
        source_handler = spec.source_spec
        tasks = spec.tasks

        for source in sources:
            yield DocumentComposer._single_runner(source, source_handler, tasks)

    @staticmethod
    def _single_runner(
        source: Source,
        spec: SourceSpec,
        tasks: dict[TaskKeyword, TaskSpec],
    ):
        uid, text = get_source_contents(source=source, spec=spec)

        # loop over the task
        components = DocumentComposer._tasks_handler(text, uid, tasks)
        document = DocumentComposer._construct_document(uid, components)
        return document

    @staticmethod
    def _tasks_handler(text, uid, tasks):
        for task_name, task_spec in tasks.items():
            comp = task_handler(
                text,
                source_uid=uid,
                task_name=task_name,
                spec=task_spec,
            )

            if comp is not None:
                yield comp

    @staticmethod
    def _construct_document(uid: str, components: Iterable[DocumentComponent]):
        components_map = {}

        for component in components:
            components_map[component.key] = component

        components_map["uid"] = uid
        return Document.model_validate(components_map)
