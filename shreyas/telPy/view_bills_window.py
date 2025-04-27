import tkinter as tk
from db_connection import get_connection

def open_view_bills_window():
    win = tk.Toplevel()
    win.title("All Bills")
    win.geometry("600x500")

    text_area = tk.Text(win, wrap="none")
    text_area.pack(expand=True, fill="both")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT b.id, c.name, b.call_minutes, b.sms_count, b.data_gb, b.total_amount, b.date FROM bills b JOIN customers c ON b.customer_id = c.id ORDER BY b.date DESC")
    bills = cursor.fetchall()
    conn.close()

    for bill in bills:
        text_area.insert(tk.END, f"Bill ID: {bill[0]}, Customer: {bill[1]}, Call: {bill[2]} mins, SMS: {bill[3]}, Data: {bill[4]} GB, Total: ₹{bill[5]}, Date: {bill[6]}\n\n")
