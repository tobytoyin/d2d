import pytest


@pytest.fixture
def valid_payload():
    return {
        "sources": [{"path": "."}, {"path": "hello-world-2.txt"}],
        "source_spec": {"provider": "mock"},
        "tasks": {
            "summary": {"provider": "mock"},
        },
    }


@pytest.fixture
def invalid_payload_sources():
    return {
        "sources": [{"path": "."}, {"paths": "invalid.txt"}],
        "source_spec": {"provider": "mock"},
        "tasks": {
            "summary": {"provider": "mock"},
        },
    }


@pytest.fixture
def invalid_payload():
    return {
        # invalid structure
        "sources": {"path": "."},
        "tasks": {
            "source_spec": {"provider": "mock"},
            "summary": {"provider": "mock"},
        },
    }


@pytest.fixture
def payload_with_invalid_task():
    return {
        "sources": [{"path": "."}],
        "source_spec": {"provider": "mock"},
        "tasks": {
            "summary": {"provider": "mock"},
            "invalid": {"provider": "none"},  # this is a invalid task indicator
        },
    }


@pytest.fixture
def payload_with_invalid_provider():
    return {
        "sources": [{"path": "."}],
        "source_spec": {"provider": "mock"},
        "tasks": {
            "summary": {"provider": "invalid"},  # this is an invalid provider
        },
    }


@pytest.fixture
def payload_with_repeated_task_indicator():
    # pylint: disable=W0109
    return {
        "sources": [{"path": "."}],
        "source_spec": {"provider": "mock"},
        "tasks": {
            "summary": {"provider": "mock"},
            "summary": {"provider": "mock"},
        },
    }
    # pylint: enable=W0109


@pytest.fixture
def payload_with_options():
    return {
        "sources": [{"path": "."}],
        "source_spec": {"provider": "mock"},
        "tasks": {
            "summary": {
                "provider": "mock",
                "options": {"option1": "val1"},
            },
        },
    }


@pytest.fixture
def payload_with_options_unpacked():
    return {
        "sources": [{"path": "."}],
        "source_spec": {"provider": "mock"},
        "tasks": {
            "summary": {
                "provider": "mock",
                "options": {"option1": "val1"},
                "options_expand": True,
            },
        },
    }
