import pytest
from utils import *


def test_no_quotes_object():
    _input = {'a': 123, 'b': "123"}
    expected = '{a: "123",b: "123"}'
    
    assert expected == no_quotes_object(_input)