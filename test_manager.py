from models.ManagerRegister import ManagerRegister
from models.PlayerManager import PlayerManager
from models.TeamManager import TeamManager
from models.MatchManager import MatchManager

# ----- Test Manager Register -----
print("\n--- Registering Manager ---")
manager = ManagerRegister(
    first_name="Ayla",
    last_name="Smith",
    username="ayla_new",  # change this
    phone_number="1234567890",
    gender="Female",
    password="pass123",
    confirm_password="pass123"
)
manager.register_manager()

# ----- Test Player Manager -----
print("\n--- Adding Player ---")
player_manager = PlayerManager()
player_manager.add_player(1, "John Doe", "Team A", "Forward")

# ----- Test Team Manager -----
print("\n--- Adding Team ---")
team_manager = TeamManager()
team_manager.add_team(
    team_name="Galatasaray",
    coach_name="Fatih Terim",
    team_country="Türkiye"
)

# ----- Test Match Manager -----
print("\n--- Adding Match ---")
match_manager = MatchManager()
match_manager.add_match(
    team1_name="Galatasaray",
    team2_name="Fenerbahçe",
    match_date="2025-05-25",
    score_team1=3,
    score_team2=2
)
