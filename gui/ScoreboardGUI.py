import tkinter as tk
from tkinter import ttk
from models.ScoreboardManager import ScoreboardManager

class ScoreboardGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Scoreboard")
        self.master.geometry("800x400")


        self.manager = ScoreboardManager()


        self.columns = ("team_name", "matches_played", "wins", "draws", "losses", "points")
        self.tree = ttk.Treeview(master, columns=self.columns, show="headings")

        for col in self.columns:
            self.tree.heading(col, text=col.replace("_", " ").title())
            self.tree.column(col, width=100, anchor=tk.CENTER)

        self.tree.pack(expand=True, fill="both")

        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        refresh_btn = tk.Button(button_frame, text="Refresh", command=self.load_scoreboard)
        refresh_btn.pack(side=tk.LEFT, padx=10)

        self.back_button = tk.Button(master, text="Back", command=self.master.destroy)
        self.back_button.pack(side=tk.LEFT, padx=10)

        self.load_scoreboard()

    def load_scoreboard(self):
        # Clear existing rows
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Fetch from DB
        data = self.manager.fetch_scoreboard()

        # Insert into treeview
        for row in data:
            self.tree.insert("", tk.END, values=tuple(row[col] for col in self.columns))
    def return_home(self):
        self.master.destroy() #close scoreboard window
        from gui.HomePageGUI import HomePageGUI
        home_window = tk.Toplevel()
        HomePageGUI(home_window)


if __name__ == "__main__":
    root = tk.Tk()
    app = ScoreboardGUI(root)
    root.mainloop()