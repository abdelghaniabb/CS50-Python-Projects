import pytest
from jar import Jar

def test_initialization():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("ten")

def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(6)  # Exceeds capacity
    with pytest.raises(ValueError):
        jar.deposit(-1)  # Invalid number of cookies

def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(3)  # Not enough cookies to withdraw
    with pytest.raises(ValueError):
        jar.withdraw(-1)  # Invalid number of cookies

def test_str():
    jar = Jar(10)
    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
