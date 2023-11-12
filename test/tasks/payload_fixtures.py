import pytest


@pytest.fixture
def valid_payload():
    return {
        "source": {
            "path": ".",
        },
        "source_reader": {"provider": "mock"},
        "tasks": {
            "summary": {"provider": "mock"},
        },
    }


@pytest.fixture
def invalid_payload():
    return {
        "sources": {
            "path": ".",
        },
        "tasks": {
            "source_reader": {"provider": "mock"},
            "summary": {"provider": "mock"},
        },
    }


@pytest.fixture
def payload_with_invalid_task():
    return {
        "source": {
            "path": ".",
        },
        "source_reader": {"provider": "mock"},
        "tasks": {
            "summary": {"provider": "mock"},
            "invalid": {"provider": "none"},  # this is a invalid task indicator
        },
    }


@pytest.fixture
def payload_with_invalid_provider():
    return {
        "source": {
            "path": ".",
        },
        "source_reader": {"provider": "mock"},
        "tasks": {
            "summary": {"provider": "invalid"},  # this is an invalid provider
        },
    }


@pytest.fixture
def payload_with_repeated_task_indicator():
    # pylint: disable=W0109
    return {
        "source": {
            "path": ".",
        },
        "source_reader": {"provider": "mock"},
        "tasks": {
            "summary": {"provider": "mock"},
            "summary": {"provider": "mock"},
        },
    }
    # pylint: enable=W0109
