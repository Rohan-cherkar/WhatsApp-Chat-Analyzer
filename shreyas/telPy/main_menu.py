import tkinter as tk

# Import functions from your other windows
from add_customer_window import open_add_customer_window
from generate_bill_window import open_generate_bill_window
from view_bills_window import open_view_bills_window
from update_delete_window import open_update_delete_window

def open_main_menu():
    root = tk.Tk()
    root.title("Telecom Billing System - Main Menu")
    root.geometry("800x500")
    root.resizable(False, False)

    tk.Label(root, text="📞 Telecom Billing System", font=("Arial", 16, "bold"), fg="#2a5d84").pack(pady=20)

    # Now link each button to its respective window
    tk.Button(root, text="Add New Customer", width=30, height=2, command=open_add_customer_window).pack(pady=10)
    tk.Button(root, text="Generate Bill", width=30, height=2, command=open_generate_bill_window).pack(pady=10)
    tk.Button(root, text="View Past Bills", width=30, height=2, command=open_view_bills_window).pack(pady=10)
    tk.Button(root, text="Update/Delete Customer", width=30, height=2, command=open_update_delete_window).pack(pady=10)

    tk.Button(root, text="Exit", width=30, height=2, bg="red", fg="white", command=root.destroy).pack(pady=20)

    root.mainloop()
