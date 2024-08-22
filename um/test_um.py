from um import count

def test_single_um():
    assert count("um") == 1
    assert count("Um, hello world") == 1
    assert count("Um, um, um.") == 3

def test_no_um():
    assert count("hello, world") == 0
    assert count("yummy") == 0
    assert count("umbrella") == 0

def test_um_with_punctuation():
    assert count("Um...") == 1
    assert count("um, um, UM!") == 3
    assert count("Well, um, that's interesting.") == 1

def test_um_with_whitespace():
    assert count("  um  ") == 1
    assert count("um\tum\num") == 3
    assert count("Um um um") == 3
