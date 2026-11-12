#Name: Kevin Child
#Class: INFO 1200
#Section: See syllabus, schedule, or Canvas course for section
#Professor: Dr. Anas AlSobeh
#Date: 11/11/2026
#Assignment #: Project 7 Part 2
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

# Import the math module to use the square root function
import tkinter as tk

# Import the messagebox module to display error messages
from tkinter import messagebox

# Import the math module to use the square root function
import math

# Define a function to calculate the length of the hypotenuse using the Pythagorean theorem
def calculate():
    a = float(side_a_entry.get())
    b = float(side_b_entry.get())
    c = math.sqrt(a**2 + b**2)

    result_label.config(text=f"Hypotenuse: {c:.2f}")

# Define a function to clear the input fields and result label
def clear():
    side_a_entry.delete(0, tk.END)
    side_b_entry.delete(0, tk.END)
    result_label.config(text="Result:")

# Create the main window
root = tk.Tk()
root.title("Pythagorean Theorem Calculator")
root.geometry("500x400")

# title label
title_label = tk.Label(root, text="Pythagorean Calculator")
title_label.pack()

# Side A label
side_a_label = tk.Label(root, text="Enter Side A:")
side_a_label.pack()

# Side A entry
side_a_entry = tk.Entry(root)
side_a_entry.pack()

# Side B label
side_b_label = tk.Label(root, text="Enter Side B:")
side_b_label.pack()

# Side B entry
side_b_entry = tk.Entry(root)
side_b_entry.pack()

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Result label
result_label = tk.Label(root, text="Result:")
result_label.pack()

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack()

# Start the main event loop
root.mainloop()
    

