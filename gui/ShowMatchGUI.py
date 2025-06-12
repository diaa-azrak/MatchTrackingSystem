import tkinter as tk
from tkinter import ttk, messagebox
from models.MatchManager import MatchManager

class ShowMatchGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Matches List")
        self.master.geometry("800x450")

        self.match_manager = MatchManager()

        title = tk.Label(master, text="All Matches", font=("Arial", 16))
        title.pack(pady=10)

        columns = ("ID", "Team 1", "Team 2", "Date", "Score 1", "Score 2")
        self.tree = ttk.Treeview(master, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor=tk.CENTER)
        self.tree.pack(fill=tk.BOTH, expand=True)

        refresh_btn = tk.Button(master, text="Refresh", command=self.load_matches)
        refresh_btn.pack(pady=10)

        self.load_matches()

    def load_matches(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        matches = self.match_manager.get_all_matches()
        if not matches:
            messagebox.showinfo("Info", "No matches found or DB connection failed.")
            return

        for match_id, team1, team2, date, score1, score2 in matches:
            self.tree.insert("", tk.END, values=(match_id, team1, team2, date, score1, score2))

if __name__ == "__main__":
    root = tk.Tk()
    app = ShowMatchesClass(root)
    root.mainloop()