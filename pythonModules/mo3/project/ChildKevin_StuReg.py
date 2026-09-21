# Name: Kevin Child Registration App
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
print("Kevin Child's Registration App")
print()

# prompt user for their first name, last name, birth year
firstName = input("First Name: ")
lastName = input("Last Name: ")
birthYear = input("Birth Year: ")
print()

# print welcome message in terminal 
print("Welcome", firstName, lastName)
print()
print("Your registration is complete.")

# create temporary password variable and print to terminal 
tempPassword = firstName + "*" + birthYear
print("Your temporary password is:", tempPassword)
