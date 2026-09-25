#!/usr/bin/env python3

# display a welcome message
print("Welcome to Kevin Child's Future Value Calculator.")
print()

# start the main program loop
choice = "y"

while choice.lower() == "y":

    # validate monthly investment
    is_valid = False

    while is_valid == False:
        monthly_investment = float(input("Enter monthly investment:\t"))

        if monthly_investment > 0 and monthly_investment <= 1000:
            is_valid = True
        else:
            print("Entry must be greater than 0 and less than or equal to 1000. Please try again.")

    # reset validation variable
    is_valid = False

    # validate yearly interest rate
    while is_valid == False:
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))

        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:
            is_valid = True
        else:
            print("Entry must be greater than 0 and less than or equal to 15. Please try again.")

    # reset validation variable
    is_valid = False

    # validate number of years
    while is_valid == False:
        years = int(input("Enter number of years:\t\t"))

        if years > 0 and years <= 50:
            is_valid = True
        else:
            print("Entry must be greater than 0 and less than or equal to 50. Please try again.")

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0

    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

    # display the result
    print("Future value:\t\t\t" + str(round(future_value, 2)))
    print()

    # ask user if they want to continue
    choice = input("Continue (y/n)? ")
    print()

# display goodbye message
print("Bye!")