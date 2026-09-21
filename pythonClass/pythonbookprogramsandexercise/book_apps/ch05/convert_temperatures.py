"""
Run the following command to run the doctests in verbose mode:
python -m doctest convert_temperatures.py -v
"""
import temperature as temp

def display_menu():
    """
    Displays the program title and menu options.

    >>> display_menu()
    The Convert Temperatures program
    <BLANKLINE>
    MENU
    1. Fahrenheit to Celsius
    2. Celsius to Fahrenheit
    <BLANKLINE>
    """
    print("The Convert Temperatures program")
    print()
    print("MENU")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print()

def convert_temp():
    """
    Converts a temperature based on user menu selection.

    >>> from unittest.mock import patch
    >>> with patch('builtins.input', side_effect=['1', '212']):
    ...     convert_temp()
    Degrees Celsius: 100.0
    >>> with patch('builtins.input', side_effect=['2', '100']):
    ...     convert_temp()
    Degrees Fahrenheit: 212.0
    >>> with patch('builtins.input', side_effect=['3']):
    ...     convert_temp()
    You must enter a valid menu number.
    """
    option = int(input("Enter a menu option: "))
    if option == 1:
        f = int(input("Enter degrees Fahrenheit: "))
        c = temp.to_celsius(f)
        c = round(c, 2)
        print("Degrees Celsius:", c)
    elif option == 2:
        c = int(input("Enter degrees Celsius: "))
        f = temp.to_fahrenheit(c)
        f = round(f, 2)
        print("Degrees Fahrenheit:", f)
    else:
        print("You must enter a valid menu number.")

def main():
    display_menu()
    again = "y"
    while again.lower() == "y":
        convert_temp()
        print()
        again = input("Convert another temperature? (y/n): ")
        print()
    print("Bye!")

if __name__ == "__main__":
    main()
