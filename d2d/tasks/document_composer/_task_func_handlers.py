# from d2d.contracts.payload import TaskPayload


# class KeywordsUndefined(Exception):
#     ...


# def execute_task_func(fn, *fn_args, task_spec: TaskPayload):
#     """Function to separate the execution step with run_tasks to allow unitest"""
#     # unpack options to function
#     if task_spec.options_expand:
#         return fn(*fn_args, **task_spec.options)

#     # function doesn't accept kwargs
#     if task_spec.options_receiver is None:
#         return fn(*fn_args)

#     passdown_kwarg = {task_spec.options_receiver: task_spec.options}

#     try:
#         return fn(*fn_args, **passdown_kwarg)
#     except TypeError as e:
#         raise KeywordsUndefined from e
