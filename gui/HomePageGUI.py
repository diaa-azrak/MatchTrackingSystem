import tkinter as tk
from tkinter import messagebox
from gui.ManagerRegisterGUI import ManagerRegisterGUI
from gui.ScoreboardGUI import ScoreboardGUI
from models.SessionManager import SessionManager

class HomePageGUI:
    def __init__(self, master, logged_in=False):
        self.master = master
        username = SessionManager.get_logged_in_manager()
        self.master.title(f"🏟 Sports Match Tracker - Welcome, {username}")
        self.master.geometry("400x550")
        self.logged_in = logged_in

        title = tk.Label(master, text="🏆 Sports Match Tracker", font=("Arial", 18, "bold"))
        title.pack(pady=20)

        if not self.logged_in:
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
            ("Logout", self.logout),
            ("Exit", master.quit)
        ]

        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        for text, command in features[:-2]:
            tk.Button(master, text=text, width=20, command=command).pack(pady=5)

        logout_button = tk.Button(master, text="Logout", width=20, command=self.logout)
        logout_button.pack(side='bottom', anchor='se', padx=10, pady=10)

        exit_button = tk.Button(master, text="Exit", width=20, command=master.quit)
        exit_button.pack(side='bottom', anchor='se', padx=10, pady=5)

    def manager_login(self):
        print("Open Manager Login Window")
        login_window = tk.Toplevel(self.master)
        from gui.ManagerLoginGUI import ManagerLoginGUI
        ManagerLoginGUI(login_window, self.master)

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
        show_matches_window = tk.Toplevel(self.master)
        from gui.ShowMatchGUI import ShowMatchGUI
        ShowMatchGUI(show_matches_window)

    def show_teams(self):
        print("Open Teams Window")
        show_teams_window = tk.Toplevel(self.master)
        from gui.ShowTeamsGUI import ShowTeamsGUI
        ShowTeamsGUI(show_teams_window)

    def show_players(self):
            print("Open Players Window")
            show_players_window = tk.Toplevel(self.master)
            from gui.ShowPlayerGUI import ShowPlayerGUI
            ShowPlayerGUI(show_players_window)

    def show_history(self):
            print("Open Match History Window")

    def show_statistics(self):
            print("Open Statistics Window")
            show_statistic_window = tk.Toplevel(self.master)
            from gui.ShowStatisticsGUI import ShowStatisticsGUI
            ShowStatisticsGUI(show_statistic_window)

    def show_cards(self):
            print("Open Cards Window")
            show_cards_window = tk.Toplevel(self.master)
            from gui.ShowCardsGUI import ShowCardsGUI
            ShowCardsGUI(show_cards_window)

    def logout(self):
        SessionManager.clear_session()
        self.master.destroy()
        login_root = tk.Tk()
        from gui.ManagerLoginGUI import ManagerLoginGUI
        ManagerLoginGUI(login_root)
        login_root.mainloop()