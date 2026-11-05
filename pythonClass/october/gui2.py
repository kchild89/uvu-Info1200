import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My GUI Application")
root.geometry("600x400")

label1 = tk.Label(root, text="Name:")
label1.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(root, text="Email:")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

def get_name():
    name = entry1.get()
    print(f"Name entered: {name}")
    messagebox.askyesno("Name Entered", f"Hello, {name}!")

button1 = tk.Button(root, text="Submit", command=get_name)
button1.grid(row=2, column=0, pady=10)

outputLabel = tk.Label(root, text="")
outputLabel.grid(row=3, column=0)


root.mainloop()