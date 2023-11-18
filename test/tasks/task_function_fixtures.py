import pytest

# We expect the Providers to be provider functions that follows the
# below function signature when passing down options
# for the providers. They should be executable by execute_spec_with_task_fncs


@pytest.fixture
def func_with_single_arg():
    def f(s):
        return s

    return f


@pytest.fixture
def func_with_args():
    def f(a, b):
        return f"{a}-{b}"

    return f


@pytest.fixture
def func_with_kwrd_receiver():
    def f(s, keyword: dict):
        val = keyword["key"]
        return f"{s}-{val}"

    return f


@pytest.fixture
def func_with_kwrd_expand():
    def f(s, key=""):
        return f"{s}-{key}"

    return f
