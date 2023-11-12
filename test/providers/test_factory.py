from d2d.providers.factory import get_task_fn


def test_get_task_fn():
    task_fn = get_task_fn("mock", "summary")
    result = task_fn("test content")
    assert result == {"result": {"content": "hello world"}, "kind": "summary"}
