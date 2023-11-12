from d2d.providers.factory import get_task_fn


def test_get_task_fn():
    task_fn = get_task_fn("mock", "summary")
    result = task_fn("test content")
    assert result == {"content": "hello world"}


def test_get_task_fn_not_exist():
    task_fn = get_task_fn("mock", "none")
    assert task_fn is None  # return as None function


def test_get_task_fn_none_provider():
    task_fn = get_task_fn("none", "summary")
