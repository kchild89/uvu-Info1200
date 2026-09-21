#!/usr/bin/env python3
"""
This module contains functions for calculating the future value 
of a series of monthly investments and for getting user input.
"""
def calculate_future_value(monthly_investment, yearly_interest, years):
    """
    Calculates the future value of a monthly investment.

    >>> calculate_future_value(0, 6, 5)
    0.0
    >>> calculate_future_value(100, 0, 1)
    1200.0
    >>> round(calculate_future_value(100, 6, 1), 2)
    1239.72
    """
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def get_float(prompt, low, high):
    """
    Prompts the user for a float within the specified range.
    Reprompts if the entry is out of range.

    >>> from unittest.mock import patch
    >>> with patch('builtins.input', side_effect=['100']):
    ...     get_float('Enter a number: ', 0, 1000)
    100.0
    >>> with patch('builtins.input', side_effect=['2000', '500']):
    ...     get_float('Enter a number: ', 0, 1000)
    Entry must be greater than 0 and less than or equal to 1000
    500.0
    """
    while True:
        number = float(input(prompt))
        if number > low and number <= high:
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high)

def get_integer(prompt, low, high):
    """
    Prompts the user for an integer within the specified range.
    Reprompts if the entry is out of range.

    >>> from unittest.mock import patch
    >>> with patch('builtins.input', side_effect=['100']):
    ...     get_integer('Enter a number: ', 0, 1000)
    100
    >>> with patch('builtins.input', side_effect=['2000', '500']):
    ...     get_integer('Enter a number: ', 0, 1000)
    Entry must be greater than 0 and less than or equal to 1000
    500
    """
    while True:
        number = int(input(prompt))
        if number > low and number <= high:
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)