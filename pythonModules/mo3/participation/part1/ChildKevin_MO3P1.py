#!/usr/bin/env python3

# name of student and app
print("Kevin Child's MPG app")

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))

# calculate miles per gallon
mpg = round(miles_driven / gallons_used, 2)
            
# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print()
print("Bye")


