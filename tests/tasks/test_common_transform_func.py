from d2d.contracts.payload import Options
from d2d.tasks.common import transform_function_with_options

from .task_function_fixtures import *

############ Test task function execution base on different signature ##########


#### below tests for correct usage ####


def test_single_param_signs(func_with_single_arg):
    opt = Options()
    fn = transform_function_with_options(func_with_single_arg, opt)
    result = fn("hello")

    assert result == "hello"


def test_args_signs(func_with_args):
    opt = Options()
    fn = transform_function_with_options(func_with_args, opt)
    result = fn("hello", "world")

    assert result == "hello-world"


def test_kwrd_receiver(func_with_kwrd_receiver):
    opt = Options(mapping={"key": "world"}, receiver="keyword")
    fn = transform_function_with_options(func_with_kwrd_receiver, opt)
    result = fn("hello")

    assert result == "hello-world"


def test_kwrd_expand(func_with_kwrd_expand):
    opt = Options(mapping={"key": "world"}, expand=True)
    fn = transform_function_with_options(func_with_kwrd_expand, opt)
    result = fn("hello")

    assert result == "hello-world"
