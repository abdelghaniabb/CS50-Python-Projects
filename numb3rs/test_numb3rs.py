#!/usr/bin/python3

from numb3rs import validate

def test_valid_addresses():
    assert validate("192.168.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("127.0.0.1") == True

def test_invalid_addresses():
    assert validate("275.3.6.28") == False
    assert validate("256.100.100.100") == False
    assert validate("192.168.1.256") == False
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.1") == False
    assert validate("192.168.01.1") == False  # Leading zero
    assert validate("192.168.1.-1") == False  # Negative number
    assert validate("192.168.1.abc") == False  # Non-numeric value
    assert validate("999.999.999.999") == False  # Out of range in all segments

def test_empty_and_non_numeric():
    assert validate("") == False
    assert validate(" ") == False
    assert validate("abc.def.ghi.jkl") == False

def test_edge_cases():
    assert validate("255.0.0.0") == True
    assert validate("0.255.255.255") == True

