import pytest

# Below contains functions with signature that is acceptable
# for the providers. They should be executable by execute_spec_with_task_fnc


def _func_with_single_arg(s):
    return s


@pytest.fixture
def func_with_single_arg():
    return _func_with_single_arg


def _func_accept_options(s, options: dict):
    _ = options
    return s


@pytest.fixture
def func_accept_options():
    return _func_accept_options


def func_with_n_args(a, b, c):
    return f"{a}, {b}, {c}"
