import pytest

from doc_uploader.utils import append_dict_iterable, no_quotes_object


def test_no_quotes_object():
    _input = {"a": 123, "b": "123"}
    expected = '{a: "123",b: "123"}'

    assert expected == no_quotes_object(_input)


def test_obj_append_new_item():
    target = {"id": 1, "item_a": [100], "item_b": ["a"]}
    update = {"id": 1, "item_a": [200], "item_b": ["b"]}

    expected = {"id": 1, "item_a": [100, 200], "item_b": ["a", "b"]}
    assert append_dict_iterable(target, update, ["item_a", "item_b"]) == expected
