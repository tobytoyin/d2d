from __future__ import annotations

from typing import Generator, Literal

from pydantic import BaseModel

from d2d.adapters.factory import get_adapter_service
from d2d.contracts.document import DocumentComponent
from d2d.contracts.source import Source


class TaskSpec(BaseModel):
    """This model contains the JSON spec as the following:

    ```json
    {
        "spec": {
            "$task_name": {
                "adapter": "$adapter_name",
                "options": "$options"
            }
        }
    }
    ```

    :param BaseModel: _description_
    :type BaseModel: _type_
    """

    spec: dict[str, AdapterSpec]


class AdapterSpec(BaseModel):
    adapter: str
    options: dict | None = None


def source_to_components(
    source: Source,
    spec: TaskSpec,
    error_handler: Literal["pass", "raise"] = "raise",
) -> Generator[tuple[str, DocumentComponent], None, None]:
    """Use a `Source` to create different `DocumentComponent` as specified

    :param source: source object to read/ load from
    :type source: Source
    :param spec: specification that indicates what Adapters and Tasks to use
    :type spec: TaskSpec
    :param error_handler: \
            indication on how error is handled when executing the spec,\ 
            defaults to "raise"
    :raises AttributeError: _description_
    :yield: ( spec_name, DocumentComponent )
    :rtype: None
    """
    for task_name, task_spec in spec.spec.items():
        try:
            service = get_adapter_service(
                adapter_name=task_spec.adapter,
                service_name=task_name,
                service_options=task_spec.options,
            )
            yield task_name, service(source)

        except AttributeError as e:
            if error_handler == "raise":
                raise AttributeError from e
            continue
