"""
Name: Kevin Child
Class: INFO 1200
Section: See the syllabus, schedule, or Canvas course
Professor: Dr. AlSobeh
Date: 2026-09-06
Assignment: Assignment 1 part 3
By submitting this assignment, I declare that the source code contained
in this assignment was written solely by me unless it was specifically
provided in the assignment. I attest that no part of this assignment,
in whole or in part, was directly created by generative AI unless its
use was explicitly permitted in the assignment instructions. I also
attest that the work was not obtained from a subscription or solution
service. I understand that unauthorized copying of source code or use
of generative AI constitutes an academic-integrity violation and may
result in a score of zero.
"""

# first name 
firstName = 'Kevin'
print('Hello, my name is ' + firstName)

# school name
schoolName = 'Utah Valley University'
print('I go to ' + schoolName)

# total credit calculation  
credits = 3
classes = 6
totalcredits = credits * classes

print('If I take 6 classes this semester and all are three credits each I will be taking ' + str(totalcredits) + ' credits')

print('I would like to save money by taking this many credits.')

# credit limit and class costs
maxCredits = 12
costPerClass = 350
classFee = 20

freeCredits = totalcredits - maxCredits
freeClasses = freeCredits / credits
totalCostPerSemester = freeClasses * (costPerClass + classFee)

print('If classes are free after the ' + str(maxCredits) + ' credits and each class cost $' + str(costPerClass) + ' (plus an additional $' + str(classFee) + ' per class fee), I will be saving $' + str(totalCostPerSemester) + ' a semester.')

totalCostPerYear = totalCostPerSemester * 3

# dislplay yearly savings 
print('That is a whopping $' + str(totalCostPerYear) + ' a year!')

# display final message 
print('This was a very informative and worth while Python assignment!')
