import tkinter as tk
from tkinter import messagebox

class InvestmentFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title = tk.Label(self, text="Investment Calculator")
        title.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Initial Investment
        tk.Label(self, text="Initial Investment ($):").grid(row=1, column=0, sticky="w")
        self.initial_var = tk.StringVar()
        tk.Entry(self, textvariable=self.initial_var).grid(row=1, column=1)
        
        # Annual Return
        tk.Label(self, text="Annual Return (%):").grid(row=2, column=0, sticky="w")
        self.return_var = tk.StringVar()
        tk.Entry(self, textvariable=self.return_var).grid(row=2, column=1)
        
        # Years
        tk.Label(self, text="Number of Years:").grid(row=3, column=0, sticky="w")
        self.years_var = tk.StringVar()
        tk.Entry(self, textvariable=self.years_var).grid(row=3, column=1)
        
        # Buttons
        tk.Button(self, text="Calculate", command=self.calculate).grid(row=4, column=0, pady=10)
        tk.Button(self, text="Clear", command=self.clear).grid(row=4, column=1, pady=10)
    
    def calculate(self):
        try:
            initial = float(self.initial_var.get())
            rate = float(self.return_var.get()) / 100
            years = int(self.years_var.get())
            
            final = initial * ((1 + rate) ** years)
            messagebox.showinfo("Result", f"Final Value: ${final:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def clear(self):
        self.initial_var.set("")
        self.return_var.set("")
        self.years_var.set("")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Investment App")
    app = InvestmentFrame(root)
    root.mainloop()

