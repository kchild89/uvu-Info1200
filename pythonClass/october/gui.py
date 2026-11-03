import tkinter as tk


def on_button_click():
    print("Button was clicked!")


def show_name():
    name = name_var.get()
    print(f"Hello, {name}!")
    outputLabel.config(text=name)


root = tk.Tk()
root.title("My GUI Application")
root.geometry("600x400")

frame = tk.Frame(root, height=100)
frame.pack()

tk.Button(frame, text="Click Me", command=on_button_click).pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack()

tk.Label(input_frame, text="Name:").grid(
    row=0, column=0, sticky="w", padx=5, pady=5
)

name_var = tk.StringVar()

tk.Entry(input_frame, textvariable=name_var).grid(
    row=0, column=1, padx=5, pady=5
)

tk.Button(root, text="Submit", command=show_name).pack()

outputLabel = tk.Label(root, text="")
outputLabel.pack()

root.mainloop()