#Name: Kevin Child
#Class: INFO 1200
#Section: See syllabus, schedule, or Canvas course for section
#Professor: Dr. Anas AlSobeh
#Date: 10/9/2026
#Assignment #: Project 5 Part 2
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

#!/usr/bin/env python3

import kcconverter as c

print("Kevin Child's Feet / Meters Converter")
print()


def fm_welcome():
    print("Kevin's Feet and Meters Converter")
    print()


def fm_menu():
    print("Conversions Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")


def main():
    fm_welcome()

    while True:
        fm_menu()

        choice = input("Select a conversion (a/b): ")
        print()

        if choice == "a":
            feet = float(input("Enter feet: "))
            meters = c.to_meters(feet)
            print(round(meters, 2), "meters")

        elif choice == "b":
            meters = float(input("Enter meters: "))
            feet = c.to_feet(meters)
            print(round(feet, 2), "feet")

        else:
            print("You did not enter a valid selection")

        more = input("Would you like to perform another conversion? (y/n): ")
        print()

        if more != "y":
            print("Thanks, bye!")
            break


if __name__ == "__main__":
    main()