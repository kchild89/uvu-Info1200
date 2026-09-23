#!/usr/bin/env python3

# display a welcome message
print("Kevin Child's Miles Per Gallon application")
print()

# create the another trip variable and set it to "y"
another_trip = "y"
# get input from the user
miles_driven = float(input("Enter miles driven:         "))
gallons_used = float(input("Enter gallons of gas used:  "))
cost_per_gallon = float(input("Cost per gallon"))

while another_trip == "y":
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon: \t", mpg)
        print("Cost Per Gallon: \t", cost_per_gallon)


    # calculate total_gas_cost
    total_gas_cost = round((gallons_used * cost_per_gallon), 1)
    print("Total Gas Cost: \t", total_gas_cost)

    # calculate cost_per_mile
    cost_per_mile = round((total_gas_cost / miles_driven), 1)
    print("Cost Per Mile: \t", cost_per_mile)

    # Display both values below the MPG result
    print("Total Gas Cost: \t", total_gas_cost)
    print("Cost Per Mile: \t", cost_per_mile)

    # Ask user for another trip
    another_trip = input("Get entries for another trip? (y/n): ")
    print()
print("Bye")



