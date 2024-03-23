#!/usr/bin/python3

from bank import value

def test_value_hello():
    assert value('hello') == 0
    assert value('HEllo how can I help you') == 0
    assert value(' hel lo there') == 0


def test_value_h():
    assert value('hi') == 20
    assert value('how are you today') == 20
    assert value('Hey man') == 20
    assert value('have a nice day') == 20


def test_value_non():
    assert value('Greeting') == 100
    assert value('good day') == 100

