from typing import Generator

from pydantic import ValidationError

from d2d.contracts.documents import DocumentComponent
from d2d.contracts.payload import SourcePayload, TaskFunctionResult
from d2d.providers.factory import get_task_fn

from .parsers import PROVIDER_INTERFACE_MAPPER
from .source_handler import get_source_text, get_source_uid


def payload_validator(payload: dict) -> SourcePayload:
    return SourcePayload.model_validate(payload)


def run_tasks(payload: dict) -> Generator[TaskFunctionResult, None, None]:
    spec = payload_validator(payload)

    # source
    source = spec.source
    source_reader = spec.source_reader
    source_text = get_source_text(provider_name=source_reader.provider, d=source)
    source_uid = get_source_uid(provider_name=source_reader.provider, d=source)

    # get the task functions from registry
    for task_name, task_spec in spec.tasks.items():
        task_fn = get_task_fn(provider_name=task_spec.provider, task_name=task_name)
        task_result = task_fn(source_text)

        yield TaskFunctionResult(
            source_uid=source_uid,
            result=task_result,
            kind=task_name,
        )


def convert_to_document_component(task_result: TaskFunctionResult) -> DocumentComponent:
    task_kind = task_result.kind
    task_result = task_result.result

    component_convertor = PROVIDER_INTERFACE_MAPPER[task_kind]
    return component_convertor(task_result)
