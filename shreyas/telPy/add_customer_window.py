import tkinter as tk
from tkinter import messagebox
from db_connection import get_connection

def add_customer():
    name = name_entry.get()
    phone = phone_entry.get()
    address = address_entry.get("1.0", tk.END).strip()

    if name and phone and address:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customers (name, phone, address) VALUES (%s, %s, %s)", (name, phone, address))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Customer added successfully!")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        address_entry.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

def open_add_customer_window():
    win = tk.Toplevel()
    win.title("Add Customer")
    win.geometry("800x500")

    tk.Label(win, text="Name").pack()
    global name_entry
    name_entry = tk.Entry(win, width=40)
    name_entry.pack()

    tk.Label(win, text="Phone").pack()
    global phone_entry
    phone_entry = tk.Entry(win, width=40)
    phone_entry.pack()

    tk.Label(win, text="Address").pack()
    global address_entry
    address_entry = tk.Text(win, height=3, width=30)
    address_entry.pack()

    tk.Button(win, text="Add", command=add_customer, bg="green", fg="white").pack(pady=10)
