"""
This module contains functions for converting temperature
between degrees Fahrenheit and degrees Celsius

Run the following command to run the doctests in verbose mode:
python -m doctest temperature.py -v
"""
def to_celsius(fahrenheit):
    """
    Accepts degrees Fahrenheit (fahrenheit parameter)
    Returns degrees Celsius

    >>> to_celsius(212)
    100.0
    >>> to_celsius(32)
    0.0
    >>> to_celsius(98.6)
    37.0
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def to_fahrenheit(celsius):
    """
    Accepts degrees Celsius (celsius parameter)
    Returns degrees Fahrenheit

    >>> to_fahrenheit(100)
    212.0
    >>> to_fahrenheit(0)
    32.0
    >>> to_fahrenheit(37)
    98.6
    """
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
