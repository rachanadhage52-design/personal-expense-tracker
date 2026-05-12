import tkinter as tk
from tkinter import messagebox

# Class
class ExpenseTracker:

    # Constructor
    def __init__(self, window):
        self.window = window
        self.window.title("Personal Expense Tracker")
        self.window.geometry("700x500")
        self.window.config(bg="#0F172A")

        heading = tk.Label(
            window,
            text="PERSONAL EXPENSE TRACKER",
            font=("Helvetica", 22, "bold"),
            bg="#0F172A",
            fg="#38BDF8"
        )
        heading.pack(pady=20)

        # Labels and Entries
        self.entry1 = self.create_field("Shopping Expenses")
        self.entry2 = self.create_field("Petrol Expenses")
        self.entry3 = self.create_field("Medical Expenses")
        self.entry4 = self.create_field("Entertainment Expenses")
        self.entry5 = self.create_field("Food Expenses")
        self.entry6 = self.create_field("Travel Expenses")

        # Button
        button = tk.Button(
            window,
            text="Calculate Total",
            command=self.costing,
            font=("Helvetica", 12, "bold"),
            bg="#38BDF8",
            fg="black",
            padx=20,
            pady=8
        )
        button.pack(pady=25)

    # Function to create label and entry
    def create_field(self, text):
        label = tk.Label(
            self.window,
            text=text,
            font=("Helvetica", 11, "bold"),
            bg="#0F172A",
            fg="white"
        )
        label.pack()

        entry = tk.Entry(
            self.window,
            width=35,
            font=("Arial", 11),
            bg="#E2E8F0"
        )
        entry.pack(pady=5)

        return entry

    # Function for total calculation
    def costing(self):
        shopping = int(self.entry1.get())
        petrol = int(self.entry2.get())
        medical = int(self.entry3.get())
        entertainment = int(self.entry4.get())
        food = int(self.entry5.get())
        travel = int(self.entry6.get())

        total = shopping + petrol + medical + entertainment + food + travel

        messagebox.showinfo(
            "Expense Tracker",
            f"Your last month Expenses = ₹{total}"
        )

# Main Window
window = tk.Tk()

# Object Creation
obj = ExpenseTracker(window)

window.mainloop()