import tkinter as tk
from tkinter import messagebox
from db_connection import get_connection

def fetch_customer():
    cid = id_entry.get()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, phone, address FROM customers WHERE id = %s", (cid,))
    data = cursor.fetchone()
    conn.close()

    if data:
        name_entry.delete(0, tk.END)
        name_entry.insert(0, data[0])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, data[1])
        address_entry.delete("1.0", tk.END)
        address_entry.insert(tk.END, data[2])
    else:
        messagebox.showinfo("Not Found", "Customer ID not found.")

def update_customer():
    cid = id_entry.get()
    name = name_entry.get()
    phone = phone_entry.get()
    address = address_entry.get("1.0", tk.END)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE customers SET name=%s, phone=%s, address=%s WHERE id=%s", (name, phone, address, cid))
    conn.commit()
    conn.close()
    messagebox.showinfo("Updated", "Customer updated.")

def delete_customer():
    cid = id_entry.get()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE id=%s", (cid,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Deleted", "Customer deleted.")

def open_update_delete_window():
    win = tk.Toplevel()
    win.title("Update/Delete Customer")
    win.geometry("350x350")

    global id_entry, name_entry, phone_entry, address_entry

    tk.Label(win, text="Customer ID").pack()
    id_entry = tk.Entry(win)
    id_entry.pack()

    tk.Button(win, text="Fetch", command=fetch_customer).pack()

    tk.Label(win, text="Name").pack()
    name_entry = tk.Entry(win)
    name_entry.pack()

    tk.Label(win, text="Phone").pack()
    phone_entry = tk.Entry(win)
    phone_entry.pack()

    tk.Label(win, text="Address").pack()
    address_entry = tk.Text(win, height=3)
    address_entry.pack()

    tk.Button(win, text="Update", command=update_customer, bg="green", fg="white").pack(pady=5)
    tk.Button(win, text="Delete", command=delete_customer, bg="red", fg="white").pack()
