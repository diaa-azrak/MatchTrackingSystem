from models.ScoreboardManager import ScoreboardManager

manager = ScoreboardManager()
scoreboard = manager.fetch_scoreboard()

for row in scoreboard:
    print(row)