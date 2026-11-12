#Name: Kevin Child
#Class: INFO 1200
#Section: See syllabus, schedule, or Canvas course for section
#Professor: Dr. Anas AlSobeh
#Date: 11/11/2026
#Assignment #: Project 7 Part 1
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

# Import the math module to use the square root function
import math

# Define a function to calculate the length of the hypotenuse using the Pythagorean theorem
def pythagoreanTheorem(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

# Prompt the user to enter the lengths of the two sides of a right triangle
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

# Calculate the length of the hypotenuse using the pythagoreanTheorem function
result = pythagoreanTheorem(a, b)
print(f"The length of the hypotenuse is: {result:.3f}")