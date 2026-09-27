# Name: Kevin Child Letter Grade Converter App
# Class: INFO 1200
# Section: See syllabus, schedule, or Canvas course for section
# Professor: AlSobeh
# Date: 2026-21-9
# Assignment #: project 4 part 1
# By submitting this assignment, I declare that the source code contained
# in this assignment was written solely by me, unless specifically provided
# in the assignment. I attest that no part of this assignment, in whole or
# in part, was directly created by Generative AI unless explicitly permitted
# by the assignment instructions, nor obtained from a subscription service.
# I understand that copying source code, in whole or in part, unless
# specifically provided in the assignment, constitutes cheating and may
# result in a zero on this assignment.

#!/usr/bin/env python3

# Display the app title and a blank line for spacing.
print("Kevin Child's Letter Grade Converter App")
print()

# Set the starting choice so the program runs at least once.
choice = "y"

# Repeat while the user enters y, allowing either uppercase or lowercase.
while choice.lower() == "y":
    # Get the numerical grade and convert it to an integer.
    i = int(input("Enter numerical grade: "))
    
    # Reject grades outside 0-100, then check cutoffs from highest to lowest.
    # Only the first matching branch runs.
    if i > 100 or i < 0:
        print("Please enter a numerical grade between 0-100")
    elif i >= 94:  # 94-100 earns an A.
        print("Letter grade: A")
        print()
    elif i >= 90:  # 90-93 earns an A-.
        print("Letter grade: A-")
        print()
    elif i >= 87:  # 87-89 earns a B+.
        print("Letter grade: B+")
        print()
    elif i >= 84:  # 84-86 earns a B.
        print("Letter grade: B")
        print()
    elif i >= 80:  # 80-83 earns a B-.
        print("Letter grade: B-")
        print()
    elif i >= 77:  # 77-79 earns a C+.
        print("Letter grade: C+")
        print()
    elif i >= 74:  # 74-76 earns a C.
        print("Letter grade: C")
        print()
    elif i >= 70:  # 70-73 earns a C-.
        print("Letter grade: C-")
        print()
    elif i >= 67:  # 67-69 earns a D+.
        print("Letter grade: D+")
        print()
    elif i >= 64:  # 64-66 earns a D.
        print("Letter grade: D")
        print()
    elif i >= 60:  # 60-63 earns a D-.
        print("Letter grade: D-")
        print()
    elif i < 60:  # 0-59 earns an E.
        print("Letter grade: E")
        print()
    else:
            # This fallback is unreachable because earlier checks cover all integers.
            print("Please Enter A numerical grade between 0-100")
            print()

    # Ask whether to convert another grade; any response other than y or Y ends the loop.
    choice: str = input("Continue? (y/n): ")
    print()

# Display a goodbye message after the user exits the loop.
print("Bye!")
