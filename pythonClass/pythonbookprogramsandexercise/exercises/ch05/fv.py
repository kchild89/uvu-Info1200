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
    """
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(1, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def get_float(prompt, low, high):
    """
    Prompts the user for a float within the specified range.
    Reprompts if the entry is out of range.

    MOCK INPUT HERE
    """
    while True:
        number = float(input(prompt))
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high)

def get_integer(prompt, low, high):
    """
    Prompts the user for an integer within the specified range.
    Reprompts if the entry is out of range.

    MOCK INPUT HERE
    """
    while True:
        number = int(input(prompt))
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)