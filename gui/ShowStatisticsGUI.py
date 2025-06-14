import tkinter as tk
from tkinter import ttk, messagebox
from models.MatchManager import MatchManager

class ShowStatisticsGUI:
    def __init__(self, master, role="User"):
        self.master = master
        self.role = role
        self.master.title("Team Statistics")
        self.master.geometry("900x450")

        self.match_manager = MatchManager()

        tk.Label(master, text="Team Statistics", font=("Arial", 18, "bold")).pack(pady=10)

        columns = ("Team", "MP", "W", "D", "L", "GF", "GA", "GD", "Points")
        self.tree = ttk.Treeview(master, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=80, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Bottom frame for Back & Refresh buttons
        bottom_frame = tk.Frame(master)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        tk.Button(bottom_frame, text="Back", command=self.master.destroy).pack(side=tk.LEFT, padx=20)
        tk.Button(bottom_frame, text="Refresh", command=self.load_statistics).pack(side=tk.RIGHT, padx=20)

        self.load_statistics()

    def load_statistics(self):
        try:
            matches = self.match_manager.get_all_matches()
            stats = {}

            for match in matches:
                try:
                    _, team1, team2, _, score1, score2 = match
                except ValueError:
                    continue

                for team in [team1, team2]:
                    if team not in stats:
                        stats[team] = {
                            "MP": 0, "W": 0, "D": 0, "L": 0,
                            "GF": 0, "GA": 0, "GD": 0, "Points": 0
                        }

                if score1 is not None and score2 is not None:
                    stats[team1]["MP"] += 1
                    stats[team2]["MP"] += 1

                    stats[team1]["GF"] += score1
                    stats[team1]["GA"] += score2
                    stats[team2]["GF"] += score2
                    stats[team2]["GA"] += score1

                    if score1 > score2:
                        stats[team1]["W"] += 1
                        stats[team2]["L"] += 1
                    elif score1 < score2:
                        stats[team2]["W"] += 1
                        stats[team1]["L"] += 1
                    else:
                        stats[team1]["D"] += 1
                        stats[team2]["D"] += 1

            for team, data in stats.items():
                data["GD"] = data["GF"] - data["GA"]
                data["Points"] = data["W"] * 3 + data["D"]

            for row in self.tree.get_children():
                self.tree.delete(row)

            if not stats:
                messagebox.showinfo("Info", "No statistics found.")
                return

            for team, data in sorted(stats.items(), key=lambda x: (x[1]["Points"], x[1]["GD"]), reverse=True):
                row = (team, data["MP"], data["W"], data["D"], data["L"],
                       data["GF"], data["GA"], data["GD"], data["Points"])
                self.tree.insert("", tk.END, values=row)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load statistics:\n{e}")

# ✅ Standalone testing
if __name__ == "__main__":
    root = tk.Tk()
    ShowStatisticsGUI(root, role="Manager")  # or "User"
    root.mainloop()
