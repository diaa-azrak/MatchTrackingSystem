import tkinter as tk
from tkinter import messagebox
from models.TeamManager import TeamManager

class ShowTeamsGUI:
    def __init__(self, root):
        self.manager = TeamManager()
        root.title("Teams List")
        root.geometry("400x500")

        self.listbox = tk.Listbox(root, width=50, height=20)
        self.listbox.pack(pady=10)

        tk.Button(root, text="Refresh", command=self.show_teams).pack(pady=5)
        self.show_teams()

    def show_teams(self):
        self.listbox.delete(0, tk.END)
        teams = self.manager.fetch_teams()

        if not teams:
            messagebox.showinfo("Info", "No teams found or DB connection failed.")
            return

        for team_name, coach_name, team_country in teams:
            display_text = f"{team_name} — Coach: {coach_name} — Country: {team_country}"
            self.listbox.insert(tk.END, display_text)

if __name__ == "__main__":
    root = tk.Tk()
    ShowTeams(root)
    root.mainloop()