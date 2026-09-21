#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, messagebox
import locale

from business import Investment

class FutureValueFrames(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        # Add the FutureValueFrames
        FutureValueFrame(parent).grid(row=0, column=0)
        FutureValueFrame(parent).grid(row=0, column=1)

        # Add the Exit button        
        ttk.Button(parent, text="Exit", command=parent.destroy).grid(
            row=1, column=1, sticky=tk.E, padx=15, pady=10)

class FutureValueFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.investment = Investment()
        self.message = ""
        
        locale.setlocale(locale.LC_ALL, 'en_US')        

        self.initComponents()

    def initComponents(self):
        # Display the grid of labels and text entry fields
        ttk.Label(self, text="Monthly Investment:").grid(
            column=0, row=0, sticky=tk.E)
        self.monthlyInvestment = tk.StringVar()
        self.monthlyInvestmentEntry = ttk.Entry(
            self, width=25, textvariable=self.monthlyInvestment)
        self.monthlyInvestmentEntry.grid(column=1, row=0)

        ttk.Label(self, text="Yearly Interest Rate:").grid(
            column=0, row=1, sticky=tk.E)
        self.yearlyRate = tk.StringVar()
        self.yearlyRateEntry = ttk.Entry(
            self, width=25, textvariable=self.yearlyRate)
        self.yearlyRateEntry.grid(column=1, row=1)

        ttk.Label(self, text="Years:").grid(
            column=0, row=2, sticky=tk.E)
        self.years = tk.StringVar()
        self.yearsEntry = ttk.Entry(self, width=25, textvariable=self.years)
        self.yearsEntry.grid(column=1, row=2)

        ttk.Label(self, text="Future Value:").grid(
            column=0, row=3, sticky=tk.E)
        self.futureValue = tk.StringVar()
        ttk.Entry(self, width=25, textvariable=self.futureValue,
            state="readonly", takefocus=False).grid(
                column=1, row=3)

        # Display the Calculate and Exit buttons
        buttonFrame = ttk.Frame(self)       #frame to hold the buttons
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        ttk.Button(buttonFrame, text="Clear",
                   command=self.clear).grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="Calculate",
                   command=self.calculate).grid(column=1, row=0)

        # Set padding for all components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    # helper method to select field
    def selectField(self, entry):
        entry.focus()
        entry.select_range(0, tk.END)

    # helper methods to convert user entry to float or int
    def getFloat(self, entry, fieldName):
        try:
            return float(entry.get())
        except ValueError:
            self.message += f"{fieldName} must be a valid number.\n"
            self.selectField(entry)

    def getInt(self, entry, fieldName):
        try:
            return int(entry.get())
        except ValueError:
            self.message += f"{fieldName} must be a valid whole number.\n"
            self.selectField(entry)

    def calculate(self):
        self.message = "" # clear any previous error message 
        
        self.investment.monthlyInvestment = self.getFloat(
            self.monthlyInvestmentEntry, "Monthly investment")
        self.investment.yearlyInterestRate = self.getFloat(
            self.yearlyRateEntry, "Yearly interest rate")
        self.investment.years = self.getInt(self.yearsEntry, "Years")

        if self.message == "": # no errors
            # calculate and display future value
            fv = self.investment.calculateFutureValue()
            currency_value = locale.currency(fv, grouping=True)
            self.futureValue.set(currency_value)
        else:
            messagebox.showerror("Error", self.message)

    def clear(self):
        self.monthlyInvestment.set("")
        self.yearlyInterestRate.set("")
        self.years.set("")
        self.futureValue.set("")
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Future Value Calculator")
    FutureValueFrames(root)
    root.mainloop()
