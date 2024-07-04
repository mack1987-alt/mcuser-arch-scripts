import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())
        interest = principal * rate * time / 100
        result_label.config(text=f"Interest: {interest:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for principal, rate, and time.")

def reset_fields():
    principal_entry.delete(0, tk.END)
    rate_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Savings Interest Calculator")

# Create labels and entries
principal_label = tk.Label(root, text="Principal Amount:")
principal_label.grid(row=0, column=0, padx=5, pady=5)
principal_entry = tk.Entry(root, width=20)
principal_entry.grid(row=0, column=1, padx=5, pady=5)

rate_label = tk.Label(root, text="Interest Rate (%):")
rate_label.grid(row=1, column=0, padx=5, pady=5)
rate_entry = tk.Entry(root, width=20)
rate_entry.grid(row=1, column=1, padx=5, pady=5)

time_label = tk.Label(root, text="Time (Years):")
time_label.grid(row=2, column=0, padx=5, pady=5)
time_entry = tk.Entry(root, width=20)
time_entry.grid(row=2, column=1, padx=5, pady=5)

# Create buttons
calculate_button = tk.Button(root, text="Calculate Interest", command=calculate_interest)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Create result label
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()