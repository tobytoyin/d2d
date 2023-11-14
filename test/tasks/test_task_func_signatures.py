from d2d.contracts.payload import TaskPayload
from d2d.tasks._taskspec_handler import execute_task_func

from .task_function_fixtures import *


############ Test task function execution base on different signature ##########
def test_single_param_signs(func_with_single_arg):
    spec = TaskPayload(provider="none")
    _ = execute_task_func(func_with_single_arg, "a", task_spec=spec)


def test_single_param_with_option_signs(func_accept_options):
    spec = TaskPayload(provider="none", options_receiver="options")
    _ = execute_task_func(func_accept_options, "a", task_spec=spec)


def test_single_param_with_incorrect_option_receiver(func_accept_options):
    spec = TaskPayload(provider="none", options_receiver="undefined")
    _ = execute_task_func(func_accept_options, "a", task_spec=spec)
