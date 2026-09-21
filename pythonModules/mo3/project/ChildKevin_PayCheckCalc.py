# Name: Kevin Child Pay Check Calculator App
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
print("Kevin Child's Pay Check Calculator App")
print() 

# prompt the user for hours worked
hoursWorked = input("Hours Worked: ")

# prompt the user for hourly pay rate
payRate = input("Hourly pay rate: ")
print()

# create a variable named grossPay & calculate
grossPay = float(hoursWorked) * float(payRate)

# display the gross pay clearly.
print("Gross pay: ", "$", grossPay, sep="")

# create a variable named taxRate and assign it the value 18.
taxRate = 18

# display the tax rate as 18%.
print("Tax Rate is: ", taxRate, "%", sep="")

# create a variable named taxAmount and calculate the tax amount
taxAmount = grossPay * (taxRate / 100)

# display the tax amount.
print("Tax Amount: ", "$", taxAmount, sep="")

# create a variable named takeHomePay
takeHomePay = grossPay - taxAmount

# display take home pay
print("Take Home Pay ", "$", round(takeHomePay, 2), sep="")