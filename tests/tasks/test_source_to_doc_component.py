from pathlib import Path

import pydantic
import pytest

from d2d.contracts import document
from d2d.contracts.source import Source
from d2d.tasks.source_to_components import TaskSpec, source_to_components

source = Source(path=Path("."), source_type="mock_type")


@pytest.fixture
def task_spec_object():
    yield {
        "spec": {
            "links": {
                "adapter": "mock_all",
                "options": {},
            },
            "metadata": {
                "adapter": "mock_all",
            },
        }
    }


def test_task_spec_converts_to_pydantic_model(task_spec_object):
    _ = TaskSpec.model_validate(task_spec_object)


def test_source_to_components_can_return_components(task_spec_object):
    spec_model = TaskSpec.model_validate(task_spec_object)

    components = dict(source_to_components(source=source, spec=spec_model))

    # test the service function returns the correct document component
    assert "links" in components.keys()
    assert "metadata" in components.keys()

    # test the service function executes and returns the correct typed object
    # that can be used to compose into a `Document` typed object
    assert isinstance(components["links"], document.DocumentComponent)
    assert isinstance(components["metadata"], document.DocumentComponent)


###### Test for Errors ######
def test_wrong_task_spec_gets_exception():
    spec = {
        "spec": {
            "links": {
                "adapters": "mock_all",  # 'adapters' key is incorrect
                "options": {},
            },
        }
    }
    with pytest.raises(pydantic.ValidationError):
        _ = TaskSpec.model_validate(spec)


def test_adapter_no_service_implemented():
    spec = {
        "spec": {
            # mock_partial has not links tasks
            "links": {
                "adapter": "mock_partial",
                "options": {},
            },
        }
    }
    spec_model = TaskSpec.model_validate(spec)
    components = source_to_components(source=source, spec=spec_model)

    with pytest.raises(AttributeError):
        dict(components)


def test_adapter_no_service_implemented_pass_error():
    spec = {
        "spec": {
            # mock_partial has not links tasks
            "links": {
                "adapter": "mock_partial",
                "options": {},
            },
            # only return this document component as it is implemented
            "summary": {
                "adapter": "mock_all",
                "options": {},
            },
        }
    }
    spec_model = TaskSpec.model_validate(spec)
    components = source_to_components(
        source=source, spec=spec_model, error_handler="pass"
    )

    components = dict(components)  # error would pass and only return 1 result
    assert len(components) == 1
