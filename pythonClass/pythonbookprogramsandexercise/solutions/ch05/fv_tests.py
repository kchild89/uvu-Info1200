import pytest
from fv import calculate_future_value, get_float, get_integer

# patch() function for mocking input() in tests
from unittest.mock import patch

# String() and redirect_stdout() for capturing print output
from io import StringIO
from contextlib import redirect_stdout


# calculate_future_value tests
def test_calculate_future_value_no_interest():
    assert calculate_future_value(100, 0, 1) == 1200.0

def test_calculate_future_value_with_interest():
    assert round(calculate_future_value(100, 6, 1), 2) == 1239.72


# get_float tests
def test_get_float_valid_input():
    with patch('builtins.input', side_effect=['500']):
        assert get_float('Enter a number: ', 0, 1000) == 500.0

def test_get_float_invalid_then_valid_input():
    with patch('builtins.input', side_effect=['2000', '500']):
        with StringIO() as buf, redirect_stdout(buf):
            number = get_float('Enter a number: ', 0, 1000)
            output = buf.getvalue()
        assert "Entry must be greater than 0" in output
        assert number == 500.0


# get_integer tests
def test_get_integer_valid_input():
    with patch('builtins.input', side_effect=['500']):
        assert get_integer('Enter an integer: ', 0, 1000) == 500

def test_get_integer_invalid_then_valid_input():
    with patch('builtins.input', side_effect=['2000', '500']):
        with StringIO() as buf, redirect_stdout(buf):
            number = get_integer('Enter an integer: ', 0, 1000)
            output = buf.getvalue()
        assert "Entry must be greater than 0" in output
        assert number == 500
        

if __name__ == "__main__":
    pytest.main([__file__, "-v"])