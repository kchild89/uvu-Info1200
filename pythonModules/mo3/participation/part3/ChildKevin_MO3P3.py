#!/usr/bin/env python3

# name of student and app
print("Kevin Child's Rectangle App")

# display a welcome message
print("The Rectangle program")
print()

# get input from the user
length = float(input("Enter the length of the triangle:\t\t"))
width = float(input("Enter the width of the triangle:\t"))

# calculate the area and perimeter of the rectangle
area = length * width
perimeter = 2 * length + 2 * width
            
# format and display the result
print("Area:\t\t" + str(area))
print("Perimeter:\t\t" + str(perimeter))

print()
print("Thanks for using this program!")


