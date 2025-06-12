import tkinter as tk
from tkinter import messagebox
from gui.ManagerRegisterGUI import ManagerRegisterGUI
from gui.ScoreboardGUI import ScoreboardGUI

class HomePageGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("🏟 Sports Match Tracker - Home")
        self.master.geometry("400x550")

        title = tk.Label(master, text="🏆 Sports Match Tracker", font=("Arial", 18, "bold"))
        title.pack(pady=20)

        tk.Button(master, text="Manager Login", width=20, command=self.manager_login).pack(pady=5)
        tk.Button(master, text="Manager Register", width=20, command=self.manager_register).pack(pady=5)

        features = [
            ("Show Matches", self.show_matches),
            ("Show Teams", self.show_teams),
            ("Show Players", self.show_players),
            ("Scoreboard", self.show_scoreboard),
            ("History Matches", self.show_history),
            ("Statistics", self.show_statistics),
            ("Cards", self.show_cards),
            ("Exit", master.quit)
        ]

        for text, command in features:
            tk.Button(master, text=text, width=20, command=command).pack(pady=5)

    def manager_login(self):
        print("Open Manager Login Window")
        login_window = tk.Toplevel(self.master)
        from gui.ManagerLoginGUI import ManagerLoginGUI
        ManagerLoginGUI(login_window)

    def manager_register(self):
        print("Open Manager Registration Window")
        register_window = tk.Toplevel(self.master)
        from gui.ManagerRegisterGUI import ManagerRegisterGUI
        ManagerRegisterGUI(register_window)

    def show_scoreboard(self):
        print("Open Scoreboard Window")
        scoreboard_window = tk.Toplevel(self.master)
        from gui.ScoreboardGUI import ScoreboardGUI
        ScoreboardGUI(scoreboard_window)

    def show_matches(self):
            print("Open Matches Window")

    def show_teams(self):
            print("Open Teams Window")

    def show_players(self):
            print("Open Players Window")

    def show_history(self):
            print("Open Match History Window")

    def show_statistics(self):
            print("Open Statistics Window")

    def show_cards(self):
            print("Open Cards Window")