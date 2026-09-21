"""
Pytest tests for the convert_temperatures module

Run the following command to install pytest:
pip install pytest

Run the following command to run the pytests in this file:
pytest convert_temperatures_test.py -v
"""
import pytest

# import the functions needed to capture output and mock input
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch

# import the module you are testing
import convert_temperatures as ct


# display_menu() tests

def test_display_menu_output():
    expected = (
        "The Convert Temperatures program\n"
        "\n"
        "MENU\n"
        "1. Fahrenheit to Celsius\n"
        "2. Celsius to Fahrenheit\n"
        "\n"
    )
    with StringIO() as buf, redirect_stdout(buf):
        ct.display_menu()
        output = buf.getvalue()
    assert output == expected


# convert_temp() tests

def test_fahrenheit_to_celsius_boiling():
    with patch("builtins.input", side_effect=["1", "212"]):
        with StringIO() as buf, redirect_stdout(buf):
            ct.convert_temp()
            output = buf.getvalue().strip()
    assert output == "Degrees Celsius: 100.0"
    assert "Celsius" in output   # more flexible test
    assert "100" in output       # more flexible test

def test_fahrenheit_to_celsius_freezing():
    with patch("builtins.input", side_effect=["1", "32"]):
        with StringIO() as buf, redirect_stdout(buf):
            ct.convert_temp()
            output = buf.getvalue().strip()
    assert output == "Degrees Celsius: 0.0"

def test_celsius_to_fahrenheit_boiling():
    with patch("builtins.input", side_effect=["2", "100"]):
        with StringIO() as buf, redirect_stdout(buf):
            ct.convert_temp()
            output = buf.getvalue().strip()
    assert output == "Degrees Fahrenheit: 212.0"

def test_celsius_to_fahrenheit_freezing():
    with patch("builtins.input", side_effect=["2", "0"]):
        with StringIO() as buf, redirect_stdout(buf):
            ct.convert_temp()
            output = buf.getvalue().strip()
    assert output == "Degrees Fahrenheit: 32.0"

def test_invalid_option():
    with patch("builtins.input", side_effect=["3"]):
        with StringIO() as buf, redirect_stdout(buf):
            ct.convert_temp()
            output = buf.getvalue().strip()
    assert output == "You must enter a valid menu number."


# main() tests

def test_main_one_conversion_then_quit():
    inputs = ["1", "212", "n"]
    with patch("builtins.input", side_effect=inputs):
        with StringIO() as buf, redirect_stdout(buf):
            ct.main()
            output = buf.getvalue()
    assert "Degrees Celsius: 100.0" in output
    assert "Bye!" in output

def test_main_two_conversions_then_quit():
    inputs = ["1", "212", "y", "2", "100", "n"]
    with patch("builtins.input", side_effect=inputs):
        with StringIO() as buf, redirect_stdout(buf):
            ct.main()
            output = buf.getvalue()
    assert "Celsius: 100" in output
    assert "Fahrenheit: 212" in output
    assert "Bye!" in output

def test_main_displays_menu():
    inputs = ["1", "32", "n"]
    with patch("builtins.input", side_effect=inputs):
        with StringIO() as buf, redirect_stdout(buf):
            ct.main()
            output = buf.getvalue()
    assert "The Convert Temperatures program" in output
    assert "MENU" in output


if __name__ == "__main__":
    pytest.main([__file__, "-v"])   # current file only, verbose mode