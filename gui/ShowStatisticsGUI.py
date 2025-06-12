import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from models.MatchManager import MatchManager  # your MatchManager import

class ShowStatisticsGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Team Statistics")
        self.master.geometry("800x400")

        self.match_manager = MatchManager()

        title_label = tk.Label(master, text="Team Statistics", font=("Arial", 18, "bold"))
        title_label.pack(pady = 10)

        columns = (
            "Team", "MP", "W", "D", "L", "GF", "GA", "GD", "Points"
        )
        self.tree = ttk.Treeview(master, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=80, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True)

        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        self.refresh_button = tk.Button(master, text="Refresh Statistic", command=self.load_statistics)
        self.refresh_button.pack(side=tk.LEFT, padx=10)

        self.back_button = tk.Button(button_frame, text = "Back", command = self.master.destroy)
        self.back_button.pack(side=tk.LEFT, padx = 10)

        # Load and show stats on start
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

                # Initialize teams in stats if not present
                for team in [team1, team2]:
                    if team not in stats:
                        stats[team] = {
                            "MP": 0, "W": 0, "D": 0, "L": 0,
                            "GF": 0, "GA": 0, "GD": 0, "Points": 0
                        }

                # Only process if both scores are not None
                if score1 is not None and score2 is not None:
                    # Update matches played
                    stats[team1]["MP"] += 1
                    stats[team2]["MP"] += 1

                    # Update goals for and against
                    stats[team1]["GF"] += score1
                    stats[team1]["GA"] += score2
                    stats[team2]["GF"] += score2
                    stats[team2]["GA"] += score1

                    # Determine win/draw/loss and points
                    if score1 > score2:
                        stats[team1]["W"] += 1
                        stats[team2]["L"] += 1
                    elif score1 < score2:
                        stats[team2]["W"] += 1
                        stats[team1]["L"] += 1
                    else:
                        stats[team1]["D"] += 1
                        stats[team2]["D"] += 1

            # Calculate goal difference and points
            for team, data in stats.items():
                data["GD"] = data["GF"] - data["GA"]
                data["Points"] = data["W"] * 3 + data["D"]

            # Clear existing data in treeview
            for row in self.tree.get_children():
                self.tree.delete(row)

            if not stats:
                messagebox.showinfo("Info", "No statistics found.")
                return

            # Insert sorted stats by points desc, then goal difference desc
            for team, data in sorted(stats.items(), key=lambda x: (x[1]["Points"], x[1]["GD"]), reverse=True):
                row = (team, data["MP"], data["W"], data["D"], data["L"], data["GF"], data["GA"], data["GD"], data["Points"])
                self.tree.insert("", tk.END, values=row)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load statistics:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShowStatisticsGUI(root)
    root.mainloop()