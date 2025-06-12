import tkinter as tk
from tkinter import ttk
from models.PlayerManager import PlayerManager

class ShowPlayerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Players List")
        self.master.geometry("700x400")

        self.player_manager = PlayerManager()

        # Title label
        title = tk.Label(master, text="All Players", font=("Arial", 16))
        title.pack(pady=10)

        # Treeview
        columns = ("ID", "Name", "Team", "Position")
        self.tree = ttk.Treeview(master, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor=tk.CENTER)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Refresh button
        refresh_btn = tk.Button(master, text="Refresh", command=self.load_players)
        refresh_btn.pack(pady=10)

        # Load data
        self.load_players()

    def load_players(self):
        # Clear old data
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Get from database
        players = self.player_manager.get_all_players()
        for player in players:
            self.tree.insert("", tk.END, values=player)

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = ShowPlayersClass(root)
    root.mainloop()