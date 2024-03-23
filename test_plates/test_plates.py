#!/usr/bin/python3

from plates import is_valid

def test_stats_2letters():
    assert is_valid('ab') == True
    assert is_valid('fdsa') == True
    assert is_valid('2dsa') == False

def test_min_string_len():
    assert is_valid('c') == False
    assert is_valid('') == False
    assert is_valid('fd') == True
    assert is_valid('dss') == True

def test_max_string_len():
    assert is_valid('as534') == True
    assert is_valid('asdd567') == False

def test_ends_numbers():
    assert is_valid('ab342') == True
    assert is_valid('as332d') == False
    assert is_valid('4234fd') == False
    assert is_valid('34245') == False

def test_first_number():
    assert is_valid('av054') == False
    assert is_valid('fv40') == True

def test_upper():
    assert is_valid('SDCa56') == True
    assert is_valid('aDa89') == True

def test_non_alphanumeric():
    assert is_valid(' abfd') == False
    assert is_valid('fg-54') == False
    assert is_valid('ds?+_') == False
