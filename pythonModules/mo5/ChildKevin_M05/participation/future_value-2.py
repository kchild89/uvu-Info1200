#!/usr/bin/env python3

# Load the validation module and refer to it as v.
import validate as v
        
# Define a function that calculates savings from monthly deposits, annual interest, and years.
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    # Divide the annual percentage by 12 and 100 to get the monthly interest rate.
    monthly_interest_rate = yearly_interest / 12 / 100
    # Multiply the number of years by 12 to get the number of months.
    months = years * 12

    # calculate future value
    # Start the future savings balance at zero.
    future_value = 0.0
    # Repeat the following steps once for each month.
    for i in range(0, months):
        # Add the monthly investment to the balance.
        future_value += monthly_investment
        # Multiply the current balance by the monthly interest rate to calculate interest.
        monthly_interest = future_value * monthly_interest_rate
        # Add the monthly interest to the balance.
        future_value += monthly_interest

    # Return the final savings balance.
    return future_value

# Define the main steps of the future value program.
def main():
    # Display the application title.
    print("Kevin Child's Validated Future Value App")
    # Display a blank line.
    print()
    # Set the starting choice to yes so the program runs at least once.
    choice = "y"
    # Repeat while the user chooses yes, ignoring capitalization.
    while choice.lower() == "y":
        # get input from the user
        # Ask for a monthly investment greater than 0 and no more than 1000.
        monthly_investment = v.get_float("Enter monthly investment:\t", 0, 1000)
        # Ask for an annual interest percentage greater than 0 and no more than 15.
        yearly_interest_rate = v.get_float("Enter yearly interest rate:\t", 0, 15)
        # Ask for a whole number of years greater than 0 and no more than 50.
        years = v.get_int("Enter number of years:\t\t", 0, 50)

        # get and display future value
        # Call the future value function and store its result.
        future_value = calculate_future_value(
            # Pass the monthly investment, annual interest rate, and number of years to the function.
            monthly_investment, yearly_interest_rate, years)

        # Round the future value to two decimal places, convert it to text, and display it.
        print("Future value:\t\t\t" + str(round(future_value, 2)))
        # Display a blank line.
        print()

        # see if the user wants to continue
        # Ask whether the user wants to perform another calculation and save the response.
        choice = input("Continue? (y/n): ")
        # Display a blank line.
        print()

    # Display a goodbye message after the user stops.
    print("Bye!")
    
# Run the main steps only when this file is executed directly.
if __name__ == "__main__":
    # Call the main function to start the program.
    main()
