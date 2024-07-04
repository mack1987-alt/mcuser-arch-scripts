import tkinter as tk
from tkinter import messagebox

def calculate_repayment():
    try:
        loan_amount = float(loan_amount_entry.get())
        interest_rate = float(interest_rate_entry.get())
        years = float(years_entry.get())
        monthly_repayment = loan_amount * (interest_rate / 100 / 12) * (1 + interest_rate / 100 / 12) ** (years * 12) / ((1 + interest_rate / 100 / 12) ** (years * 12) - 1)
        result_label.config(text=f"Monthly Repayment: {monthly_repayment:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for loan amount, interest rate, and years.")

def reset_fields():
    loan_amount_entry.delete(0, tk.END)
    interest_rate_entry.delete(0, tk.END)
    years_entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Loan Repayment Calculator")

# Create labels and entries
loan_amount_label = tk.Label(root, text="Loan Amount:")
loan_amount_label.grid(row=0, column=0, padx=5, pady=5)
loan_amount_entry = tk.Entry(root, width=20)
loan_amount_entry.grid(row=0, column=1, padx=5, pady=5)

interest_rate_label = tk.Label(root, text="Interest Rate (%):")
interest_rate_label.grid(row=1, column=0, padx=5, pady=5)
interest_rate_entry = tk.Entry(root, width=20)
interest_rate_entry.grid(row=1, column=1, padx=5, pady=5)

years_label = tk.Label(root, text="Years:")
years_label.grid(row=2, column=0, padx=5, pady=5)
years_entry = tk.Entry(root, width=20)
years_entry.grid(row=2, column=1, padx=5, pady=5)

# Create buttons
calculate_button = tk.Button(root, text="Calculate Repayment", command=calculate_repayment)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Create result label
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()