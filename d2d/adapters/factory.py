import d2d.adapters.mock as mock


def get_adapter_service(
    adapter_name: str,
    service_name: str,
):
    adapter = {
        "mock_all": mock.MockSourceTasks_All,
        "mock_partial": mock.MockSourceTasks_Partial,
        # "obsidian": obsidian.SourceHandlers,
    }.get(adapter_name.lower())

    try:
        service = getattr(adapter, service_name.lower())
    except AttributeError as e1:
        err_msg = f'"{adapter_name}" adapter does not have a "{service_name}" task'
        raise AttributeError(err_msg) from e1

    return service
