import tkinter as tk
from tkinter import ttk, messagebox
from models.PlayerManager import PlayerManager

class ShowPlayerGUI:
    def __init__(self, master, role="User"):
        self.master = master
        self.role = role
        self.master.title("Players List")
        self.master.geometry("750x480")

        self.player_manager = PlayerManager()

        tk.Label(master, text="All Players", font=("Arial", 16)).pack(pady=10)

        columns = ("ID", "Name", "Team", "Position")
        self.tree = ttk.Treeview(master, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=160, anchor=tk.CENTER)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Button frame under the treeview
        middle_frame = tk.Frame(master)
        middle_frame.pack(fill=tk.X, pady=5)

        if self.role == "Manager":
            tk.Button(middle_frame, text="Add Player", command=self.add_player).pack(side=tk.LEFT, padx=5)
            tk.Button(middle_frame, text="Update Selected", command=self.update_player).pack(side=tk.LEFT, padx=5)
            tk.Button(middle_frame, text="Delete Selected", command=self.delete_player).pack(side=tk.LEFT, padx=5)

        # Bottom Frame: Refresh & Back
        bottom_frame = tk.Frame(master)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        tk.Button(bottom_frame, text="Back", command=self.master.destroy).pack(side=tk.LEFT, padx=20)
        tk.Button(bottom_frame, text="Refresh", command=self.load_players).pack(side=tk.RIGHT, padx=20)

        self.load_players()

    def load_players(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        players = self.player_manager.get_all_players()
        for player in players:
            self.tree.insert("", tk.END, values=player)

    def get_selected_player(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a player.")
            return None
        return self.tree.item(selected[0])["values"]

    def add_player(self):
        def save():
            pid = id_entry.get()
            name = name_entry.get()
            team = team_entry.get()
            pos = pos_entry.get()

            if not all([pid, name, team, pos]):
                messagebox.showerror("Error", "All fields are required.")
                return

            try:
                self.player_manager.add_player(pid, name, team, pos)
                messagebox.showinfo("Success", "Player added.")
                win.destroy()
                self.load_players()
            except Exception as e:
                messagebox.showerror("Error", f"Add failed: {e}")

        win = tk.Toplevel(self.master)
        win.title("Add New Player")

        tk.Label(win, text="Player ID").pack(); id_entry = tk.Entry(win); id_entry.pack()
        tk.Label(win, text="Name").pack(); name_entry = tk.Entry(win); name_entry.pack()
        tk.Label(win, text="Team").pack(); team_entry = tk.Entry(win); team_entry.pack()
        tk.Label(win, text="Position").pack(); pos_entry = tk.Entry(win); pos_entry.pack()

        tk.Button(win, text="Save", command=save).pack(pady=10)

    def update_player(self):
        selected = self.get_selected_player()
        if not selected:
            return
        pid, old_name, old_team, old_pos = selected

        def save():
            name = name_entry.get()
            team = team_entry.get()
            pos = pos_entry.get()
            try:
                self.player_manager.update_player(pid, name, team, pos)
                messagebox.showinfo("Success", "Player updated.")
                win.destroy()
                self.load_players()
            except Exception as e:
                messagebox.showerror("Error", f"Update failed: {e}")

        win = tk.Toplevel(self.master)
        win.title("Update Player")

        tk.Label(win, text="Name").pack(); name_entry = tk.Entry(win); name_entry.insert(0, old_name); name_entry.pack()
        tk.Label(win, text="Team").pack(); team_entry = tk.Entry(win); team_entry.insert(0, old_team); team_entry.pack()
        tk.Label(win, text="Position").pack(); pos_entry = tk.Entry(win); pos_entry.insert(0, old_pos); pos_entry.pack()

        tk.Button(win, text="Update", command=save).pack(pady=10)

    def delete_player(self):
        selected = self.get_selected_player()
        if not selected:
            return

        pid = selected[0]
        confirm = messagebox.askyesno("Confirm", "Delete selected player?")
        if confirm:
            try:
                self.player_manager.delete_player(pid)
                messagebox.showinfo("Deleted", "Player deleted.")
                self.load_players()
            except Exception as e:
                messagebox.showerror("Error", f"Delete failed: {e}")

# ✅ Standalone test launcher
if __name__ == "__main__":
    root = tk.Tk()
    ShowPlayerGUI(root, role="Manager")  # Use role="User" for read-only mode
    root.mainloop()
