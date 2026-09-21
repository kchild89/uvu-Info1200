"""
Pytests for the temperature module

Run the following command to install pytest:
pip install pytest

Run the following command to run the tests:
pytest temperature_test.py -v
"""
import pytest
from temperature import to_celsius, to_fahrenheit


# to_celsius() tests

# Standard conversions
def test_to_celsius_boiling():
    assert to_celsius(212) == 100.0

def test_to_celsius_freezing():
    assert to_celsius(32) == 0.0

def test_to_celsius_body_temp():
    assert to_celsius(98.6) == 37.0

# Edge cases
def test_to_celsius_below_freezing():
    assert to_celsius(31) < 0.0

def test_to_celsius_above_freezing():
    assert to_celsius(33) > 0.0

def test_to_celsius_negative_fahrenheit():
    assert to_celsius(-40) == -40.0

def test_to_celsius_absolute_zero():
    assert to_celsius(-459.67) == -273.15

# Return type
def test_to_celsius_returns_float():
    assert isinstance(to_celsius(212), float)

# Inverse relationship
def test_to_celsius_inverse_of_to_fahrenheit():
    assert to_celsius(to_fahrenheit(25)) == 25.0


# to_fahrenheit() tests

# Standard conversions
def test_to_fahrenheit_boiling():
    assert to_fahrenheit(100) == 212.0

def test_to_fahrenheit_freezing():
    assert to_fahrenheit(0) == 32.0

def test_to_fahrenheit_body_temp():
    assert to_fahrenheit(37) == 98.6

# Edge cases
def test_to_fahrenheit_below_freezing():
    assert to_fahrenheit(-1) < 32.0

def test_to_fahrenheit_above_freezing():
    assert to_fahrenheit(1) > 32.0

def test_to_fahrenheit_negative_forty():
    assert to_fahrenheit(-40) == -40.0

def test_to_fahrenheit_absolute_zero():
    assert to_fahrenheit(-273.15) == pytest.approx(-459.67)

# Return type
def test_to_fahrenheit_returns_float():
    assert isinstance(to_fahrenheit(0), float)

# Inverse relationship
def test_to_fahrenheit_inverse_of_to_celsius():
    assert to_fahrenheit(to_celsius(72)) == 72.0


if __name__ == "__main__":
    pytest.main()                 # all files, default mode
    # pytest.main(["-v"])           # all files, verbose mode
    # pytest.main([__file__])       # current file, default mode
    # pytest.main([__file__, "-v"])   # current file, verbose mode
