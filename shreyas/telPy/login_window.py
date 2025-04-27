import tkinter as tk
from tkinter import messagebox
import main_menu  # This will be your main dashboard file

# Hardcoded admin credentials (you can modify this or later link to a DB)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

def check_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        root.destroy()
        main_menu.open_main_menu()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Login UI
root = tk.Tk()
root.title("Admin Login")
root.geometry("800x500")
root.resizable(False, False)

tk.Label(root, text="Admin Login", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=check_login, bg="#007bff", fg="white").pack(pady=10)

root.mainloop()
    