import logging
from collections import namedtuple
from functools import cache
from typing import Any, Generator, Iterable

from pydantic import ValidationError

from d2d.contracts.documents import Document, DocumentComponent
from d2d.contracts.payload import TaskFunctionResult, TaskKeyword, TaskSpec
from d2d.providers.factory import get_task_fn
from d2d.tasks.common import transform_function_with_options

# from ._component_convertors import ConvertorsMapper
# from .document_composer._source_handler import get_source_text, get_source_uid
# from .document_composer._task_func_handlers import execute_task_func


def task_runner(
    *args,
    source_uid: str,
    task_name: TaskKeyword,
    spec: TaskSpec,
) -> TaskFunctionResult | None:
    """Retrieve the task function from the catalog and transform function for exec

    :param task_name: _description_
    :type task_name: str
    :param spec: _description_
    :type spec: TaskPayload
    :return: _description_
    :rtype: _type_
    """
    fn = get_task_fn(provider_name=spec.provider, task_name=task_name)

    if fn is None:
        return

    fn = transform_function_with_options(fn, options=spec.options)
    result = fn(*args)

    return TaskFunctionResult(
        source_uid=source_uid,
        result=result,
        kind=task_name,
    )


# def convert_to_document_component(task_result: TaskFunctionResult) -> DocumentComponent:
#     """Convert task_function dictionary results into DcoumentComponent object

#     :param task_result: _description_
#     :type task_result: TaskFunctionResult
#     :return: _description_
#     :rtype: DocumentComponent
#     """
#     task_kind = task_result.kind
#     task_result = task_result.result

#     component_convertor = getattr(ConvertorsMapper, task_kind)
#     return component_convertor(task_result)


# def components_to_document(
#     uid: str,
#     components: Iterable[DocumentComponent],
# ) -> Document:
#     components_map = {"uid": uid}

#     for component in components:
#         components_map[component.key] = component

#     return Document.model_validate(components_map)
