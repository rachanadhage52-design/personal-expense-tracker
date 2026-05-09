import tkinter as tk
from tkinter import messagebox

def costing():

    shopping = int(entry1.get())
    petrol = int(entry2.get())
    medical = int(entry3.get())
    entertainment = int(entry4.get())
    food = int(entry5.get())
    trip = int(entry6.get())

    total_expenses = (shopping + petrol + medical + entertainment + food + trip)

    total = f"{total_expenses} expenses"

    messagebox.showinfo("Expense Tracker",total)

#Main Window
window = tk.Tk()
window.title("Personal Expense Tracker")
window.geometry("900x450")

# Shopping
track1 = tk.Label(window, text="Shopping Expenses")
track1.pack()
entry1 = tk.Entry(window)
entry1.pack()

# Petrol
track2 = tk.Label(window, text="Petrol Expenses")
track2.pack()
entry2 = tk.Entry(window)
entry2.pack()

# Medical
track3 = tk.Label(window, text="Medical Expenses")
track3.pack()
entry3 = tk.Entry(window)
entry3.pack()

# Entertainment
track4 = tk.Label(window, text="Entertainment Expenses")
track4.pack()
entry4 = tk.Entry(window)
entry4.pack()

# Food
track5 = tk.Label(window, text="Food Expenses")
track5.pack()
entry5 = tk.Entry(window)
entry5.pack()

# Trip
track6 = tk.Label(window, text="Trip Expenses")
track6.pack()
entry6 = tk.Entry(window)
entry6.pack()

# Button
button = tk.Button(window,text="Track Your Total",command=costing)

button.pack()
window.mainloop()