import tkinter as tk
from tkinter import messagebox
from models.ManagerLogin import ManagerLogin
from gui.ManagerRegisterGUI import ManagerRegisterGUI
from gui.HomePageGUI import HomePageGUI

class ManagerLoginGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Manager Login")
        self.master.geometry("300x250")

        tk.Label(master, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        tk.Label(master, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        tk.Button(master, text="Login", command=self.login).pack(pady=10)
        tk.Button(master, text="Register", command=self.open_register_window).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        manager = ManagerLogin(username, password)
        if manager.login():
            messagebox.showinfo("Success", "Login Successful")
            self.master.destroy()  # Optionally move to another screen

            home_root = tk.Tk()
            HomePageGUI(home_root)
            home_root.mainloop()
        else:
            messagebox.showerror("Error", "Login Failed")

    def open_register_window(self):
        register_window = tk.Toplevel(self.master)
        ManagerRegisterGUI(register_window)