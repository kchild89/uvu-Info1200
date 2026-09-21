# Name: Kevin Child Letter Grade Converter App
# Class: INFO 1200
# Section: See syllabus, schedule, or Canvas course for section
# Professor: AlSobeh
# Date: 2026-21-9
# Assignment #: project 4
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
print("Kevin Child's Letter Grade Converter App")
print()

# Set the starting choice so the program runs at least once.
choice = "y"

# Repeat while the user enters y, allowing either uppercase or lowercase.
while choice.lower() == "y":
    # Get the numerical grade and convert it to an integer.
    i = int(input("Enter Numerical Grade: "))
    
    # Check the grade range and display the matching letter grade.
    if i >= 0 and i <= 59:
        print("E")
    elif i >= 60 and i <= 63:
        print("D-")
    elif i >= 64 and i <= 66:
        print("D")
    elif i >= 67 and i <= 69:
        print("D+")
    elif i >= 70 and i <= 73:
        print("C-")
    elif i >= 74 and i <= 76:
        print("C")
    elif i >= 77 and i <= 79:
        print("C+")
    elif i >= 80 and i <= 83:
        print("B-")
    elif i >= 84 and i <= 86:
        print("B")
    elif i >= 87 and i <= 89:
        print("B+")
    elif i >= 90 and i <= 93:
        print("A-")
    elif i >= 94 and i <= 100:
        print("A")
    else:
        # Display an error message for grades outside the valid range.
        print("Please Enter A Numerical Grade Between 0-100")

    # Ask whether the user wants to convert another grade.
    choice = input("Continue? (y/n): ") 
   
