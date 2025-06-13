import tkinter as tk
from tkinter import messagebox
from models.ManagerLogin import ManagerLogin
from gui.ManagerRegisterGUI import ManagerRegisterGUI
from gui.HomePageGUI import HomePageGUI
from models.SessionManager import SessionManager


class ManagerLoginGUI:
    def __init__(self, master, home_window=None):
        self.master = master
        self.home_window = home_window
        self.master.title("Manager Login")
        self.master.geometry("300x250")

        tk.Label(master, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        tk.Label(master, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        tk.Button(master, text="Login", command=self.login).pack(pady=10)

        self.register_label = tk.Label(master, text="Don't have an account? Register here.", fg="blue", cursor="hand2")
        self.register_label.pack(pady=5)

        self.register_label.bind("<Button-1>", self.open_register_window)
        tk.Button(master, text="Register", command=self.open_register_window).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        manager = ManagerLogin(username, password)
        if manager.login():
            SessionManager.set_logged_in_manager(username)
            messagebox.showinfo("Success", "Login Successful")
            self.master.destroy()  # Optionally move to another screen

            if self.home_window:
                self.home_window.destroy()

            home_root = tk.Tk()
            HomePageGUI(home_root, logged_in=True)
            home_root.mainloop()
        else:
            messagebox.showerror("Error", "Login Failed")

    def open_register_window(self, event=None):
        """Open the Register window. 'event=None' allows both button click to call this"""
        register_window = tk.Toplevel(self.master)
        ManagerRegisterGUI(register_window)