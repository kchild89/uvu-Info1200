# Name: Kevin Child Tip Calculator App
# Class: INFO 1200
# Section: See syllabus, schedule, or Canvas course for section
# Professor: AlSobeh
# Date: 2026-21-9
# Assignment #: project 4 part 2
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

mealCost = input("Cost of Meal: ")

for percentage in range(15, 26, 5):
    print(str(percentage) + "%") 