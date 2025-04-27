import tkinter as tk
from customer_module import add_customer
from billing_module import generate_bill
from view_customers_window import open_view_customers_window  # Add this import


def save_customer():
    name = name_entry.get()
    phone = phone_entry.get()
    address = address_entry.get("1.0", tk.END).strip()
    
    if name and phone and address:
        add_customer(name, phone, address)
        status_label.config(text="✅ Customer added successfully!", fg="green")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        address_entry.delete("1.0", tk.END)
    else:
        status_label.config(text="❌ Please fill all fields", fg="red")

def calculate_bill():
    try:
        cid = int(customer_id_entry.get())
        minutes = int(call_entry.get())
        sms = int(sms_entry.get())
        data = float(data_entry.get())
        total = generate_bill(cid, minutes, sms, data)
        bill_status_label.config(text=f"✅ Bill Generated: ₹{total:.2f}", fg="green")

        # Clear fields
        customer_id_entry.delete(0, tk.END)
        call_entry.delete(0, tk.END)
        sms_entry.delete(0, tk.END)
        data_entry.delete(0, tk.END)

    except Exception as e:
        bill_status_label.config(text=f"❌ Error: {e}", fg="red")

# Main Window
root = tk.Tk()
root.title("Telecom Billing System")
root.geometry("420x600")
root.resizable(False, False)

title = tk.Label(root, text="📞 Telecom Billing System", font=("Arial", 16, "bold"), fg="#2a5d84")
title.pack(pady=10)

# --- Add Customer Section ---
tk.Label(root, text="--- Add New Customer ---", font=("Arial", 12, "bold")).pack(pady=5)

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Text(root, height=3, width=30)
address_entry.pack()

tk.Button(root, text="Add Customer", command=save_customer, bg="#0099cc", fg="white").pack(pady=5)
status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack()



# --- Billing Section ---
tk.Label(root, text="\n--- Generate Bill ---", font=("Arial", 12, "bold")).pack(pady=5)

tk.Label(root, text="Customer ID").pack()
customer_id_entry = tk.Entry(root, width=40)
customer_id_entry.pack()

tk.Label(root, text="Call Minutes").pack()
call_entry = tk.Entry(root, width=40)
call_entry.pack()

tk.Label(root, text="SMS Count").pack()
sms_entry = tk.Entry(root, width=40)
sms_entry.pack()

tk.Label(root, text="Data Usage (in GB)").pack()
data_entry = tk.Entry(root, width=40)
data_entry.pack()

tk.Button(root, text="Generate Bill", command=calculate_bill, bg="#28a745", fg="white").pack(pady=5)
bill_status_label = tk.Label(root, text="", font=("Arial", 10))
bill_status_label.pack()

root.mainloop()
