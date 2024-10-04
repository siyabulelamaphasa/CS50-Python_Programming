from fuel import convert, gauge
import pytest

# // Test the convert function
def test_convert():
    assert convert("1/4") == 25
    assert convert("4/4") == 100

    # // Pytest the convert function (checks for errors)
    with pytest.raises(ValueError):
        convert("three/four")

    with pytest.raises(ZeroDivisionError):
        convert("4/0")

# // Test the gauge function
def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
