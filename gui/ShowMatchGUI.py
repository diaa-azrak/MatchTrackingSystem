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

        # Frame for buttons
        button_frame = tk.Frame(master)
        button_frame.pack(fill=tk.X, pady=10)

        # Refresh button in center
        refresh_btn = tk.Button(button_frame, text="Refresh", command=self.load_matches)
        refresh_btn.pack(side=tk.TOP)

        # Back button at right
        back_btn = tk.Button(button_frame, text="Back", command=self.master.destroy)
        back_btn.pack(side=tk.LEFT, padx=10)

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

    def return_home(self):
        self.master.destroy()
        try:
            from gui.HomePageGUI import HomePageGUI
            home_window = tk.Tk()
            HomePageGUI(home_window)
            home_window.mainloop()
        except ImportError:
            print("HomePageGUI could not be loaded (possibly running directly).")

# Allow running independently for testing
if __name__ == "__main__":
    root = tk.Tk()
    app = ShowMatchGUI(root)
    root.mainloop()
