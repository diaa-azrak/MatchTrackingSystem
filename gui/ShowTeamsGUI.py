import tkinter as tk
from tkinter import ttk, messagebox
from models.TeamManager import TeamManager

class ShowTeamsGUI:
    def __init__(self, root):
        self.root = root
        self.manager = TeamManager()
        self.root.title("Teams List")
        self.root.geometry("600x400")

        title_label = tk.Label(root, text="Teams Information", font=("Arial", 14))
        title_label.pack(pady=10)

        # Treeview
        self.columns = ("team_name", "coach_name", "team_country")
        self.tree = ttk.Treeview(root, columns=self.columns, show="headings")
        self.tree.heading("team_name", text="Team Name")
        self.tree.heading("coach_name", text="Coach")
        self.tree.heading("team_country", text="Country")

        for col in self.columns:
            self.tree.column(col, width=180, anchor=tk.CENTER)

        self.tree.pack(expand=True, fill="both", padx=10, pady=5)

        # Refresh button (placed in the middle after the tree)
        refresh_btn = tk.Button(root, text="Refresh", command=self.show_teams)
        refresh_btn.pack(pady=5)

        # Bottom frame for the Back button
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        back_btn = tk.Button(bottom_frame, text="Back", command=self.root.destroy)
        back_btn.pack(side=tk.LEFT, padx=20)

        self.show_teams()

    def show_teams(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        teams = self.manager.fetch_teams()

        if not teams:
            messagebox.showinfo("Info", "No teams found or DB connection failed.")
            return

        for team_name, coach_name, team_country in teams:
            self.tree.insert("", tk.END, values=(team_name, coach_name, team_country))


if __name__ == "__main__":
    root = tk.Tk()
    ShowTeamsGUI(root)
    root.mainloop()