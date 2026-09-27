# Name: Kevin Child Change App
# Class: INFO 1200
# Section: See syllabus, schedule, or Canvas course for section
# Professor: AlSobeh
# Date: 2026-27-9
# Assignment #: project 4 part 3
# By submitting this assignment, I declare that the source code contained
# in this assignment was written solely by me, unless specifically provided
# in the assignment. I attest that no part of this assignment, in whole or
# in part, was directly created by Generative AI unless explicitly permitted
# by the assignment instructions, nor obtained from a subscription service.
# I understand that copying source code, in whole or in part, unless
# specifically provided in the assignment, constitutes cheating and may
# result in a zero on this assignment.

#!/usr/bin/env python3

# display name and app
print("Kevin Child's Change App")
print()

# Start with "y" so the change calculator runs at least once.
choice = "y"

# Repeat while the user enters "y" or "Y" to continue.
while choice.lower() == "y":
    # Get the number of cents and convert the input to an integer.
    cents = int(input("Enter number of cents (0-99): "))
    print()
    # Count quarters using integer division, then keep the remaining cents.
    quarters = cents // 25
    cents = cents % 25
    
    # Count dimes from the remaining cents and update the remainder.
    dimes = cents // 10 
    cents = cents % 10

    # Count nickels from the remaining cents and update the remainder.
    nickels = cents // 5
    cents = cents % 5

    # Use pennies for any cents left after counting the larger coins.
    pennies = cents // 1
    cents = cents % 1    

    # Display the number of each coin needed to make the change.
    print("Quarters: ", quarters)
    print("Dimes: ", dimes)
    print("Nickels: ", nickels)
    print("Pennies: ", pennies)
    print()
    # Ask whether to calculate change for another amount.
    choice = input("Continue? (y/n): ")
    print()

# Display a goodbye message when the user exits the loop.
print("Bye!")
