from functools import partial
from typing import Callable

from d2d.contracts.payload import Options


def transform_function_with_options(
    fn: Callable,
    options: Options | None,
) -> Callable:
    """Inject the Options payload into a function

    :param fn: _description_
    :type fn: function
    :param options: _description_
    :type options: _type_
    """
    if not options:
        return partial(fn)

    if options.mapping is None:
        return partial(fn)

    if options.expand is True:
        return partial(fn, **options.mapping)

    if options.receiver is None:
        return partial(fn)

    # finally use fn(*args, receiver=mapping)
    pass_down_kwargs = {options.receiver: options.mapping}
    return partial(fn, **pass_down_kwargs)
