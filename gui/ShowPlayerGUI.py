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
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Refresh button (centered below the tree)
        refresh_btn = tk.Button(master, text="Refresh", command=self.load_players)
        refresh_btn.pack(pady=5)

        # Bottom frame for the Back button
        bottom_frame = tk.Frame(master)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        back_btn = tk.Button(bottom_frame, text="Back", command=self.master.destroy)
        back_btn.pack(side=tk.LEFT, padx=20)

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
    app = ShowPlayerGUI(root)
    root.mainloop()