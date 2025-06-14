import tkinter as tk
from tkinter import ttk, messagebox
from models.TeamManager import TeamManager

class ShowTeamsGUI:
    def __init__(self, root, role="User"):
        self.root = root
        self.role = role
        self.manager = TeamManager()

        self.root.title("Teams List")
        self.root.geometry("700x450")

        tk.Label(root, text="Teams Information", font=("Arial", 14)).pack(pady=10)

        self.columns = ("team_id", "team_name", "coach_name", "team_country")
        self.tree = ttk.Treeview(root, columns=self.columns, show="headings")

        headers = {
            "team_id": "ID",
            "team_name": "Team Name",
            "coach_name": "Coach",
            "team_country": "Country"
        }

        for col in self.columns:
            self.tree.heading(col, text=headers[col])
            self.tree.column(col, width=150, anchor=tk.CENTER)

        self.tree.pack(expand=True, fill="both", padx=10, pady=5)

        # Manager-only buttons
        if self.role == "Manager":
            btn_frame = tk.Frame(root)
            btn_frame.pack(pady=5)

            tk.Button(btn_frame, text="Add Team", command=self.add_team).pack(side=tk.LEFT, padx=5)
            tk.Button(btn_frame, text="Update Selected", command=self.update_team).pack(side=tk.LEFT, padx=5)
            tk.Button(btn_frame, text="Delete Selected", command=self.delete_team).pack(side=tk.LEFT, padx=5)

        # Universal buttons
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(fill=tk.X, pady=10)

        tk.Button(bottom_frame, text="Refresh", command=self.show_teams).pack(side=tk.RIGHT, padx=20)
        tk.Button(bottom_frame, text="Back", command=self.root.destroy).pack(side=tk.LEFT, padx=20)

        self.show_teams()

    def show_teams(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        teams = self.manager.fetch_teams()
        if not teams:
            messagebox.showinfo("Info", "No teams found or DB connection failed.")
            return

        for team_id, name, coach, country in teams:
            self.tree.insert("", tk.END, values=(team_id, name, coach, country))

    def get_selected_team(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a team.")
            return None
        return self.tree.item(selected[0])["values"]

    def add_team(self):
        def save():
            name = name_entry.get()
            coach = coach_entry.get()
            country = country_entry.get()

            if not all([name, coach, country]):
                messagebox.showerror("Error", "All fields are required.")
                return

            self.manager.add_team(name, coach, country)
            messagebox.showinfo("Success", "Team added.")
            win.destroy()
            self.show_teams()

        win = tk.Toplevel(self.root)
        win.title("Add New Team")

        tk.Label(win, text="Team Name").pack(); name_entry = tk.Entry(win); name_entry.pack()
        tk.Label(win, text="Coach").pack(); coach_entry = tk.Entry(win); coach_entry.pack()
        tk.Label(win, text="Country").pack(); country_entry = tk.Entry(win); country_entry.pack()
        tk.Button(win, text="Save", command=save).pack(pady=10)

    def update_team(self):
        selected = self.get_selected_team()
        if not selected:
            return
        team_id, old_name, old_coach, old_country = selected

        def save():
            name = name_entry.get()
            coach = coach_entry.get()
            country = country_entry.get()

            self.manager.update_team(team_id, name, coach, country)
            messagebox.showinfo("Success", "Team updated.")
            win.destroy()
            self.show_teams()

        win = tk.Toplevel(self.root)
        win.title("Update Team")

        tk.Label(win, text="Team Name").pack(); name_entry = tk.Entry(win); name_entry.insert(0, old_name); name_entry.pack()
        tk.Label(win, text="Coach").pack(); coach_entry = tk.Entry(win); coach_entry.insert(0, old_coach); coach_entry.pack()
        tk.Label(win, text="Country").pack(); country_entry = tk.Entry(win); country_entry.insert(0, old_country); country_entry.pack()
        tk.Button(win, text="Update", command=save).pack(pady=10)

    def delete_team(self):
        selected = self.get_selected_team()
        if not selected:
            return

        team_id = selected[0]
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this team?")
        if confirm:
            self.manager.delete_team(team_id)
            messagebox.showinfo("Deleted", "Team deleted successfully.")
            self.show_teams()

# Allow running standalone
if __name__ == "__main__":
    root = tk.Tk()
    ShowTeamsGUI(root, role="Manager")  # Change to "User" for read-only test
    root.mainloop()
