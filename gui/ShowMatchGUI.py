import tkinter as tk
from tkinter import ttk, messagebox
from models.MatchManager import MatchManager

class ShowMatchGUI:
    def __init__(self, master, role="User"):
        self.master = master
        self.role = role
        self.master.title("Matches List")
        self.master.geometry("900x500")

        self.match_manager = MatchManager()

        tk.Label(master, text="All Matches", font=("Arial", 16)).pack(pady=10)

        columns = ("ID", "Team 1", "Team 2", "Date", "Score 1", "Score 2")
        self.tree = ttk.Treeview(master, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor=tk.CENTER)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Frame below the tree for action buttons
        action_frame = tk.Frame(master)
        action_frame.pack(fill=tk.X, pady=10)

        # Left side: Manager-only controls
        if self.role == "Manager":
            tk.Button(action_frame, text="Add Match", command=self.add_match).pack(side=tk.LEFT, padx=5)
            tk.Button(action_frame, text="Update Selected", command=self.update_match).pack(side=tk.LEFT, padx=5)
            tk.Button(action_frame, text="Delete Selected", command=self.delete_match).pack(side=tk.LEFT, padx=5)

        # Right side: Universal controls
        tk.Button(action_frame, text="Back", command=self.master.destroy).pack(side=tk.RIGHT, padx=20)
        tk.Button(action_frame, text="Refresh", command=self.load_matches).pack(side=tk.RIGHT, padx=20)

        self.load_matches()

    def load_matches(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        matches = self.match_manager.get_all_matches()
        if not matches:
            messagebox.showinfo("Info", "No matches found or DB connection failed.")
            return

        for match in matches:
            self.tree.insert("", tk.END, values=match)

    def get_selected_match(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select Match", "Please select a match.")
            return None
        return self.tree.item(selected[0])["values"]

    def add_match(self):
        def save():
            t1 = entry_team1.get()
            t2 = entry_team2.get()
            date = entry_date.get()
            s1 = entry_score1.get().strip()
            s2 = entry_score2.get().strip()

            if not all([t1, t2, date]):
                messagebox.showerror("Error", "Team names and match date are required.")
                return

            try:
                score1 = int(s1) if s1 else None
                score2 = int(s2) if s2 else None

                self.match_manager.add_match(t1, t2, date, score1, score2)
                messagebox.showinfo("Success", "Match added.")
                win.destroy()
                self.load_matches()
            except ValueError:
                messagebox.showerror("Error", "Scores must be numbers or left blank.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add match: {e}")

        win = tk.Toplevel(self.master)
        win.title("Add Match")

        for label in ["Team 1", "Team 2", "Date (YYYY-MM-DD)", "Score 1", "Score 2"]:
            tk.Label(win, text=label).pack()
        entry_team1 = tk.Entry(win); entry_team1.pack()
        entry_team2 = tk.Entry(win); entry_team2.pack()
        entry_date = tk.Entry(win); entry_date.pack()
        entry_score1 = tk.Entry(win); entry_score1.pack()
        entry_score2 = tk.Entry(win); entry_score2.pack()

        tk.Button(win, text="Save", command=save).pack(pady=10)

    def update_match(self):
        match = self.get_selected_match()
        if not match:
            return
        match_id, t1_old, t2_old, date_old, s1_old, s2_old = match

        def save_update():
            t1 = entry_team1.get()
            t2 = entry_team2.get()
            date = entry_date.get()
            s1 = entry_score1.get()
            s2 = entry_score2.get()

            try:
                self.match_manager.update_match(match_id, t1, t2, date, int(s1), int(s2))
                messagebox.showinfo("Success", "Match updated.")
                win.destroy()
                self.load_matches()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update match: {e}")

        win = tk.Toplevel(self.master)
        win.title("Update Match")

        tk.Label(win, text="Team 1").pack()
        entry_team1 = tk.Entry(win); entry_team1.insert(0, t1_old); entry_team1.pack()

        tk.Label(win, text="Team 2").pack()
        entry_team2 = tk.Entry(win); entry_team2.insert(0, t2_old); entry_team2.pack()

        tk.Label(win, text="Date (YYYY-MM-DD)").pack()
        entry_date = tk.Entry(win); entry_date.insert(0, date_old); entry_date.pack()

        tk.Label(win, text="Score 1").pack()
        entry_score1 = tk.Entry(win); entry_score1.insert(0, s1_old); entry_score1.pack()

        tk.Label(win, text="Score 2").pack()
        entry_score2 = tk.Entry(win); entry_score2.insert(0, s2_old); entry_score2.pack()

        tk.Button(win, text="Update", command=save_update).pack(pady=10)

    def delete_match(self):
        match = self.get_selected_match()
        if not match:
            return

        match_id = match[0]
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this match?")
        if confirm:
            try:
                self.match_manager.delete_match(match_id)
                messagebox.showinfo("Deleted", "Match deleted successfully.")
                self.load_matches()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete match: {e}")

# ✅ Standalone testing
if __name__ == "__main__":
    root = tk.Tk()
    ShowMatchGUI(root, role="Manager")  # Or role="User"
    root.mainloop()
