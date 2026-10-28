#!/usr/bin/env python3

tax = 0.06  # Store the sales tax rate of 6% as a decimal.

def sales_tax(total):  # Define a function that calculates the sales tax on a total.
    tax_amount = total * tax  # Multiply the total by the tax rate to find the tax amount.
    return tax_amount  # Return the calculated tax amount to the caller.

def main():  # Define the main function that runs the calculator.
    print("Sales Tax Calculator\n")  # Display the program title followed by a blank line.
    total = float(input("Enter total: "))  # Ask for the total and convert the input to a floating-point number.
    total_after_tax = round(total + sales_tax(total), 2)  # Add the sales tax to the total and round to two decimal places.
    print("Total after tax: ", total_after_tax)  # Display the total including sales tax.
    
if __name__ == "__main__":  # Check whether this file is being run directly.
    main()  # Call the main function to start the calculator.
