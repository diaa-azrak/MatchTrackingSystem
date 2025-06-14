import tkinter as tk
from tkinter import messagebox
from models.LoginHandler import LoginHandler
from gui.RegisterHandlerGUI import RegisterHandlerGUI
from gui.HomePageGUI import HomePageGUI
from models.SessionManager import SessionManager

class LoginGUI:
    def __init__(self, master, home_window=None):
        self.master = master
        self.home_window = home_window
        self.master.title("Login")
        self.master.geometry("300x300")

        tk.Label(master, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        tk.Label(master, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.role_var = tk.StringVar(value="User")
        tk.Label(master, text="Select Role").pack(pady=5)
        for text, value in [("User", "User"), ("Manager", "Manager")]:
            tk.Radiobutton(master, text=text, variable=self.role_var, value=value).pack()

        tk.Button(master, text="Login", command=self.login).pack(pady=10)

        self.register_label = tk.Label(master, text="Don't have an account? Register here.", fg="blue", cursor="hand2")
        self.register_label.pack(pady=5)
        self.register_label.bind("<Button-1>", self.open_register_window)

        tk.Button(master, text="Register", command=self.open_register_window).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_var.get()

        handler = LoginHandler(username, password, role)
        success, message = handler.login()

        if success:
            SessionManager.set_logged_in_manager(username)
            final_role = handler.get_role()
            messagebox.showinfo("Success", message)
            self.master.destroy()
            if self.home_window:
                self.home_window.destroy()

            home_root = tk.Tk()
            HomePageGUI(home_root, logged_in=True, role=final_role)
            home_root.mainloop()
        else:
            messagebox.showerror("Login Failed", message)

    def open_register_window(self, event=None):
        RegisterHandlerGUI(tk.Toplevel(self.master))
