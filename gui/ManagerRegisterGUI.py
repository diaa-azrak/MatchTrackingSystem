import tkinter as tk
from tkinter import messagebox
from models.ManagerRegister import ManagerRegister

class ManagerRegisterGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Register Manager")
        self.master.geometry("400x500")

        self.entries = {}

        fields = ["First Name", "Last Name", "Username", "Phone", "Gender", "Password", "Confirm Password"]
        for field in fields:
            tk.Label(master, text=field).pack(pady=2)
            show = "*" if "Password" in field else ""
            entry = tk.Entry(master, show=show)
            entry.pack()
            self.entries[field] = entry

        tk.Button(master, text="Register", command=self.register).pack(pady=10)

    def register(self):
        data = {field: self.entries[field].get() for field in self.entries}
        manager = ManagerRegister(
            data["First Name"],
            data["Last Name"],
            data["Username"],
            data["Phone"],
            data["Gender"],
            data["Password"],
            data["Confirm Password"]
        )
        manager.register_manager()
        messagebox.showinfo("Done", "Manager registered. You can now log in.")
        self.master.destroy()