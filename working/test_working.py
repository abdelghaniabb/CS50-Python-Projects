from working import convert
import pytest

def test_valid_cases():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("1:30 PM to 2:45 PM") == "13:30 to 14:45"
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"

def test_invalid_cases():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")  # Invalid hour
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")  # Invalid minute
    with pytest.raises(ValueError):
        convert("9 AM to 5:00 PM to 7:00 PM")  # Invalid format

def test_edge_cases():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("11:59 AM to 12:01 PM") == "11:59 to 12:01"

