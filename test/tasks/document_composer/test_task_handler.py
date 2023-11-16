from d2d.contracts.payload import TaskSpec
from d2d.tasks.document_composer._task_handler import TaskFunctionResult, task_runner


def test_task_runner():
    mock_source_text = "duumy content"
    mock_uid = "mock-id"
    spec = TaskSpec(provider="mock")

    result = task_runner(
        mock_source_text,
        source_uid=mock_uid,
        task_name="summary",
        spec=spec,
    )
    assert result == TaskFunctionResult(
        source_uid=mock_uid,
        result={"content": "hello world"},
        kind="summary",
    )


def test_task_runner_passes_when_error():
    mock_source_text = "duumy content"
    mock_uid = "mock-id"
    spec = TaskSpec(provider="mock")

    result = task_runner(
        mock_source_text,
        source_uid=mock_uid,
        task_name="none",  # type: ignore
        spec=spec,
    )
    assert result is None
