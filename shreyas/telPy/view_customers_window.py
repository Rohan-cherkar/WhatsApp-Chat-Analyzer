import tkinter as tk
from db_connection import get_connection

def open_view_customers_window():
    win = tk.Toplevel()
    win.title("View All Customers")
    win.geometry("600x400")

    # Create a scrollable text area
    text_area = tk.Text(win, wrap="none", height=15, width=80)
    text_area.pack(expand=True, fill="both")

    # Fetch customer data from the database
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone, address FROM customers ORDER BY name")
    customers = cursor.fetchall()
    conn.close()

    # Insert customer data into the text area
    if customers:
        for customer in customers:
            text_area.insert(tk.END, f"ID: {customer[0]}, Name: {customer[1]}, Phone: {customer[2]}, Address: {customer[3]}\n\n")
    else:
        text_area.insert(tk.END, "No customers found.\n")
