import tkinter as tk
from tkinter import messagebox
from typing import Optional
from models.SessionManager import SessionManager

class HomePageGUI:
    def __init__(self, master, logged_in: bool = False, role: Optional[str] = None):
        self.master = master
        self.role = role
        self.logged_in = logged_in

        username = SessionManager.get_logged_in_manager()
        self.master.title(f"🏟 Sports Match Tracker - Welcome, {username}")
        self.master.geometry("400x500")

        title = tk.Label(master, text="🏆 Sports Match Tracker", font=("Arial", 18, "bold"))
        title.pack(pady=20)

        if self.role:
            role_label = tk.Label(master, text=f"Logged in as: {self.role}", font=("Arial", 12))
            role_label.pack(pady=5)

        if not self.logged_in:
            tk.Button(master, text="Login", width=20, command=self.manager_login).pack(pady=5)
            tk.Button(master, text="Register", width=20, command=self.manager_register).pack(pady=5)

        features = [
            ("Show Matches", self.show_matches),
            ("Show Teams", self.show_teams),
            ("Show Players", self.show_players),
            ("Scoreboard", self.show_scoreboard),
            ("Statistics", self.show_statistics),
        ]

        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        for text, command in features:
            tk.Button(button_frame, text=text, width=20, command=command).pack(pady=5)

        logout_button = tk.Button(master, text="Logout", width=20, command=self.logout)
        logout_button.pack(side='bottom', anchor='se', padx=10, pady=10)

        exit_button = tk.Button(master, text="Exit", width=20, command=self.exit_app)
        exit_button.pack(side='bottom', anchor='se', padx=10, pady=5)

    def manager_login(self):
        login_window = tk.Toplevel(self.master)
        from gui.LoginGUI import LoginGUI
        LoginGUI(login_window, self.master)

    def manager_register(self):
        register_window = tk.Toplevel(self.master)
        from gui.RegisterHandlerGUI import RegisterHandlerGUI
        RegisterHandlerGUI(register_window)

    def show_scoreboard(self):
        scoreboard_window = tk.Toplevel(self.master)
        from gui.ScoreboardGUI import ScoreboardGUI
        ScoreboardGUI(scoreboard_window)

    def show_matches(self):
        show_matches_window = tk.Toplevel(self.master)
        from gui.ShowMatchGUI import ShowMatchGUI
        ShowMatchGUI(show_matches_window, role=self.role)

    def show_teams(self):
        show_teams_window = tk.Toplevel(self.master)
        from gui.ShowTeamsGUI import ShowTeamsGUI
        ShowTeamsGUI(show_teams_window, role=self.role)

    def show_players(self):
        show_players_window = tk.Toplevel(self.master)
        from gui.ShowPlayerGUI import ShowPlayerGUI
        ShowPlayerGUI(show_players_window, role=self.role)

    def show_statistics(self):
        show_statistic_window = tk.Toplevel(self.master)
        from gui.ShowStatisticsGUI import ShowStatisticsGUI
        ShowStatisticsGUI(show_statistic_window, role=self.role)

    def logout(self):
        SessionManager.clear_session()
        self.master.destroy()
        login_root = tk.Tk()
        from gui.LoginGUI import LoginGUI
        LoginGUI(login_root)
        login_root.mainloop()

    def exit_app(self):
        self.master.destroy()  # Proper app shutdown
