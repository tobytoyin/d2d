from collections import namedtuple
from functools import cache
from typing import Generator, Iterable

from pydantic import ValidationError

from d2d.contracts.documents import Document, DocumentComponent
from d2d.contracts.payload import SourcePayload, TaskFunctionResult
from d2d.providers.factory import get_task_fn

from ._component_convertors import ConvertorsMapper
from ._source_handler import get_source_text, get_source_uid

SourceMetaItems = namedtuple("SourceMetaItems", "source_uid source_text")


def payload_validator(payload: dict) -> SourcePayload:
    """To validate the raw incoming JSON payload matches the format\
        and return it as Pydantic model

    :param payload: _description_
    :type payload: dict
    :return: _description_
    :rtype: SourcePayload
    """
    return SourcePayload.model_validate(payload)


@cache
def unpack_source_items(spec: SourcePayload) -> SourceMetaItems:
    source = spec.source
    source_reader = spec.source_reader
    source_text = get_source_text(provider_name=source_reader.provider, d=source)
    source_uid = get_source_uid(provider_name=source_reader.provider, d=source)
    return SourceMetaItems(source_uid, source_text)


def run_tasks(spec: SourcePayload) -> Generator[TaskFunctionResult, None, None]:
    """With the Source contents, interact with Providers' interface's task functions

    :param spec: _description_
    :type spec: SourcePayload
    :yield: _description_
    :rtype: Generator[TaskFunctionResult, None, None]
    """
    source_uid, source_text = unpack_source_items(spec)

    # get the task functions from registry
    for task_name, task_spec in spec.tasks.items():
        task_fn = get_task_fn(provider_name=task_spec.provider, task_name=task_name)

        # skip the execution when task_fn cannot be called
        if task_fn is None:
            # TODO write logs
            continue

        task_result = task_fn(source_text)

        yield TaskFunctionResult(
            source_uid=source_uid,
            result=task_result,
            kind=task_name,
        )


def convert_to_document_component(task_result: TaskFunctionResult) -> DocumentComponent:
    """Convert task_function dictionary results into DcoumentComponent object

    :param task_result: _description_
    :type task_result: TaskFunctionResult
    :return: _description_
    :rtype: DocumentComponent
    """
    task_kind = task_result.kind
    task_result = task_result.result

    component_convertor = getattr(ConvertorsMapper, task_kind)
    return component_convertor(task_result)


def components_to_document(
    uid: str,
    components: Iterable[DocumentComponent],
) -> Document:
    components_map = {"uid": uid}

    for component in components:
        components_map[component.key] = component

    return Document.model_validate(components_map)
