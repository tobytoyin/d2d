from __future__ import annotations

import logging
from collections import namedtuple
from functools import cache
from typing import Any, Generator, Iterable

from pydantic import ValidationError

from d2d.contracts.documents import Document, DocumentComponent
from d2d.contracts.payload import TaskFunctionResult, TaskKeyword, TaskSpec
from d2d.providers.factory import get_task_fn
from d2d.tasks.common import transform_function_with_options

from ._component_adapters import TaskFunctionsAdapters

# from .document_composer._source_handler import get_source_text, get_source_uid
# from .document_composer._task_func_handlers import execute_task_func


def task_handler(
    *args_to_task_fn, source_uid: str, task_name: TaskKeyword, spec: TaskSpec
) -> DocumentComponent | None:
    """Retrieve the task function from the catalog and transform function for exec

    :param source_uid: _description_
    :type source_uid: str
    :param task_name: _description_
    :type task_name: TaskKeyword
    :param spec: _description_
    :type spec: TaskSpec
    :return: _description_
    :rtype: DocumentComponent
    """
    result = _task_runner(
        *args_to_task_fn,
        source_uid=source_uid,
        task_name=task_name,
        spec=spec,
    )

    if result is None:
        logging.warning("result is incompatible")
        return

    return _convert_to_document_component(result)


def _task_runner(
    *args_to_task_fn,
    source_uid: str,
    task_name: TaskKeyword,
    spec: TaskSpec,
) -> TaskFunctionResult | None:
    fn = get_task_fn(provider_name=spec.provider, task_name=task_name)

    if fn is None:
        return

    fn = transform_function_with_options(fn, options=spec.options)
    result = fn(*args_to_task_fn)

    return TaskFunctionResult(
        source_uid=source_uid,
        result=result,
        kind=task_name,
    )


def _convert_to_document_component(result: TaskFunctionResult) -> DocumentComponent:
    component_convertor = getattr(TaskFunctionsAdapters, result.kind)
    return component_convertor(result.result)
