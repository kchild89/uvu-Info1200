import tkinter as tk
from tkinter import messagebox

def show_greeting():
    name = name_entry.get()
    messagebox.showinfo("Greeting", f"Hello, {name}!")

root = tk.Tk()
root.title("Greeting Application")
root.geometry("400x400")

name_label = tk.Label(root, text="Enter your name:")
name_label.grid(row=0, column=0, padx=10, pady=10)

age_label = tk.Label(root, text="Enter your age:")
age_label.grid(row=1, column=0, padx=10, pady=10)

email_label = tk.Label(root, text="Enter your email:")
email_label.grid(row=2, column=0, padx=10, pady=10)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=10)

email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=10)

greet_button = tk.Button(root, text="Submit", command=show_greeting)
greet_button.grid(row=3, column=0, columnspan=2, pady=10)

canvas = tk.Canvas(root, width=400, height=200)
canvas.grid(row=4, column=0, columnspan=2)

root.mainloop()