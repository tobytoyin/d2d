from d2d.tasks.document_composer import _component_adapters


def test_summary_composer():
    payload = {"content": "mock summary"}

    summary = _component_adapters.summary_adapter(payload)

    assert summary.content == "mock summary"


def test_summary_composer_wrong_format():
    payload = {"contents": "mock summary"}

    summary = _component_adapters.summary_adapter(payload)

    assert summary.content == ""


def test_summary_composer_extra_fields_skip():
    payload = {
        "content": "mock summary",
        "extra": "skip",
    }

    summary = _component_adapters.summary_adapter(payload)

    assert "extra" not in summary.model_fields
    assert "content" in summary.model_fields
