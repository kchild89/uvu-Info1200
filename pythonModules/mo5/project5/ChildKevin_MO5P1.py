#Name: Kevin Child
#Class: INFO 1200
#Section: See syllabus, schedule, or Canvas course for section
#Professor: Dr. Anas AlSobeh
#Date: 10/9/2026
#Assignment #: Project 5 Part 1
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

#!/usr/bin/env python3

def is_even(num):
    if num % 2 == 0:
        return True 
    else:
        return False

def main():
    print("Kevin's even or odd checker")
    print()

    my_num = int(input("Enter an integer:\t"))

    if is_even(my_num):
        print("This is an even number")
    else:
        print("This is an odd number") 


if __name__ == "__main__":
    main()