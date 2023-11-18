def append_dict_iterable(target: dict, new: dict, append_keys) -> dict:
    target = target.copy()
    for key in append_keys:
        target[key] += new[key]

    return target
