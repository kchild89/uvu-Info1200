import tkinter as tk  # Import tkinter for the GUI
from tkinter import messagebox  # Import messagebox for popup messages

def show_greeting():  # Function to display a greeting
    name = name_entry.get()  # Get the name entered by the user
    messagebox.showinfo("Greeting", f"Hello, {name}!")  # Display greeting message

root = tk.Tk()  # Create the main window
root.title("Greeting Application")  # Set the window title
root.geometry("400x400")  # Set the window size

name_label = tk.Label(root, text="Enter your name:")  # Create name label
name_label.grid(row=0, column=0, padx=10, pady=10)  # Position name label

age_label = tk.Label(root, text="Enter your age:")  # Create age label
age_label.grid(row=1, column=0, padx=10, pady=10)  # Position age label

email_label = tk.Label(root, text="Enter your email:")  # Create email label
email_label.grid(row=2, column=0, padx=10, pady=10)  # Position email label

name_entry = tk.Entry(root)  # Create name input field
name_entry.grid(row=0, column=1, padx=10, pady=10)  # Position name input field

age_entry = tk.Entry(root)  # Create age input field
age_entry.grid(row=1, column=1, padx=10, pady=10)  # Position age input field

email_entry = tk.Entry(root)  # Create email input field
email_entry.grid(row=2, column=1, padx=10, pady=10)  # Position email input field

greet_button = tk.Button(root, text="Submit", command=show_greeting)  # Create submit button
greet_button.grid(row=3, column=0, columnspan=2, pady=10)  # Position submit button

root.mainloop()  # Keep the application running