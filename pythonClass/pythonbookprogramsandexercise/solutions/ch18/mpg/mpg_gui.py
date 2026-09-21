#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, messagebox

class MPGFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.message = ""
        self.pack()

        # Display the grid of components
        ttk.Label(self, text="Miles Driven:").grid(
            column=0, row=0, sticky=tk.E)
        self.miles = tk.StringVar()
        self.milesEntry = ttk.Entry(self, width=30, textvariable=self.miles)
        self.milesEntry.grid(column=1, row=0)

        ttk.Label(self, text="Gallons of Gas Used:").grid(
            column=0, row=1, sticky=tk.E)
        self.gallons = tk.StringVar()
        self.gallonsEntry = ttk.Entry(self, width=30, textvariable=self.gallons)
        self.gallonsEntry.grid(column=1, row=1)

        ttk.Label(self, text="Miles Per Gallon:").grid(
            column=0, row=2, sticky=tk.E)
        self.milesPerGallon = tk.StringVar()
        ttk.Entry(self, width=30, textvariable=self.milesPerGallon,
                  state="readonly", takefocus=False).grid(
                      column=1, row=2)

        ttk.Button(self, text="Calculate", command=self.calculate).grid(
            column=1, row=3, sticky=tk.E)

        # Add padding to all components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

        # Set focus on first text entry field
        self.milesEntry.focus()

    def selectField(self, entry):
        entry.focus()
        entry.select_range(0, tk.END)
            
    def getFloat(self, entry, fieldName):
        try:
            return float(entry.get())
        except ValueError:
            self.message += f"{fieldName} must be a valid number.\n"
            self.selectField(entry)
            
    def calculate(self):
        self.message = "" # clear any previous error message
        
        # Get numbers from the first two text entry fields
        miles_driven = self.getFloat(self.milesEntry, "Miles driven")
        gallons_used = self.getFloat(self.gallonsEntry, "Gallons of gas used")

        if self.message == "":
            # Calculate the miles per gallon (mpg)
            mpg = miles_driven / gallons_used
            mpg = round(mpg, 2)

            # Display the miles per gallon in the third text field
            self.milesPerGallon.set(mpg)
        else:
            messagebox.showerror("Error", self.message)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Miles Per Gallon Calculator")
    MPGFrame(root)
    root.mainloop()
