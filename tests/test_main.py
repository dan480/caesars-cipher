import pytest
from src.encoding import encoding_func


def test_encoding_func():
    result = encoding_func("", "alphabet", 2)
    assert result == ""
