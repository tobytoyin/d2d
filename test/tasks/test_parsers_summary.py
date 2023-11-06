from d2d.tasks import parsers


def test_summary_composer():
    payload = {"content": "mock summary"}

    summary = parsers.summary_composer(payload)

    assert summary.content == "mock summary"


def test_summary_composer_wrong_format():
    payload = {"contents": "mock summary"}

    summary = parsers.summary_composer(payload)

    assert summary.content == ""


def test_summary_composer_extra_fields_skip():
    payload = {
        "content": "mock summary",
        "extra": "skip",
    }

    summary = parsers.summary_composer(payload)

    assert "extra" not in summary.model_fields
    assert "content" in summary.model_fields
