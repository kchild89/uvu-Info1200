# Name: Kevin Child Tip Calculator App
# Class: INFO 1200
# Section: See syllabus, schedule, or Canvas course for section
# Professor: AlSobeh
# Date: 2026-16-9
# Assignment #: project 3
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
print("Kevin Child's Tip Calculator App")
print()

# prompt the user for the cost of the meal 
costOfMeal = input("Cost of Meal: ")

# prompt the user for the tip percentage and store it in tipPercentage
tipPercentage = input("Tip Percentage: ")
print()

# create a variable named tipAmount and calculate
tipAmount = float(costOfMeal) * (float(tipPercentage) / 100)

# create a variable for the total amount and calculate
totalAmount = round(float(costOfMeal), 2) + round(tipAmount, 2)

# display both the tip amount and final total rounded
print("Tip Amount: $", round(tipAmount, 2), sep="")
print("Total Amount: $", round(totalAmount, 2), sep="")