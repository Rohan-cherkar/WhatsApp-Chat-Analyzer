import tkinter as tk
from tkinter import messagebox
from db_connection import get_connection

def generate_bill():
    try:
        cid = int(customer_id_entry.get())
        call = int(call_entry.get())
        sms = int(sms_entry.get())
        data = float(data_entry.get())

        # Billing logic (e.g., ₹1 per minute, ₹0.5 per SMS, ₹10 per GB)
        total = call * 1 + sms * 0.5 + data * 10

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bills (customer_id, call_minutes, sms_count, data_gb, total_amount) VALUES (%s, %s, %s, %s, %s)",
                       (cid, call, sms, data, total))
        conn.commit()
        conn.close()

        messagebox.showinfo("Bill Generated", f"Total: ₹{total:.2f}")
        customer_id_entry.delete(0, tk.END)
        call_entry.delete(0, tk.END)
        sms_entry.delete(0, tk.END)
        data_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_generate_bill_window():
    win = tk.Toplevel()
    win.title("Generate Bill")
    win.geometry("800x500")

    tk.Label(win, text="Customer ID").pack()
    global customer_id_entry
    customer_id_entry = tk.Entry(win, width=30)
    customer_id_entry.pack()

    tk.Label(win, text="Call Minutes").pack()
    global call_entry
    call_entry = tk.Entry(win, width=30)
    call_entry.pack()

    tk.Label(win, text="SMS Count").pack()
    global sms_entry
    sms_entry = tk.Entry(win, width=30)
    sms_entry.pack()

    tk.Label(win, text="Data Usage (GB)").pack()
    global data_entry
    data_entry = tk.Entry(win, width=30)
    data_entry.pack()

    tk.Button(win, text="Generate", command=generate_bill, bg="blue", fg="white").pack(pady=10)
