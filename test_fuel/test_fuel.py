#!/usr/bin/python3

import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("0/1") == 0
    assert convert("1/1") == 100

    with pytest.raises(ValueError):
        convert("2/1")  # X is greater than Y
    with pytest.raises(ValueError):
        convert("a/b")  # Non-integer values
    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # Denominator is zero


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"

if __name__ == '__main__':
    pytest.main()
