
from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_h():
    assert value("hi") == 20
    assert value("Hey") == 20
    assert value("h") == 20
    assert value("H") == 20

def test_other():
    assert value("goodbye") == 100
    assert value("xyz") == 100
    assert value("123") == 100
    assert value(" ") == 100

def test_empty_string():
    assert value("") == 100

if __name__ == "__main__":
    test_hello()
    test_h()
    test_other()
    test_empty_string()
    print("All tests passed!")
