from d2d.contracts.payload import TaskSpec
from d2d.tasks.document_composer._task_handler import task_runner


def test_task_runner():
    mock_source_text = "duumy content"
    spec = TaskSpec(provider="mock")

    result = task_runner(mock_source_text, task_name="summary", spec=spec)
    assert result == {"content": "hello world"}
