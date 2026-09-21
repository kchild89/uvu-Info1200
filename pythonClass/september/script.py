# prompt user for age 
age = int(input("Enter your age to determine your ticket price: "))

# determine ticket price based on age
if age > 0 and age <= 12:
    print("Your ticket price is $8.00")
elif age > 12 and age <= 17:
    print("Your ticket price is $12.00")
elif age > 17 and age <= 64:
    print("Your ticket price is $15.00")
else:
    print("Your ticket price is $10.00")

number = 1
while number <= 100:
    print(number)
    number += 1






