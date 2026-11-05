import tkinter as tk
from tkinter import messagebox

def show_greeting():
    name = name_entry.get()
    messagebox.showinfo("Greeting", f"Hello, {name}!")

root = tk.Tk()
root.title("Greeting Application")
root.geometry("300x200")

name_label = tk.Label(root, text="Enter your name:")
name_label.pack(pady=10)



name_entry = tk.Entry(root)
name_entry.pack(pady=5)

greet_button = tk.Button(root, text="Submit", command=show_greeting)
greet_button.pack(pady=10)

root.mainloop()