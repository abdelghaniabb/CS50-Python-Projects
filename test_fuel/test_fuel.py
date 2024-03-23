#!/usr/bin/python3

from fuel import convert, gauge

def test_convert():
    assert convert('1/2') == 50
    assert convert('2/2') == 100
    try:
        convert('3/0')
    except ZeroDivisionError as e:
        assert str(e) == "Y cannot be 0"

def test_gauge():
    assert gauge(0.5) == 'E'
    assert gauge(10.4) == '10%'
    assert gauge(99) == 'F'
