from models.RegisterHandler import ManagerRegister
from models.PlayerManager import PlayerManager
from models.TeamManager import TeamManager
from models.MatchManager import MatchManager

# ----- Test Manager Register -----
#print("\n--- Registering Manager ---")
#manager = ManagerRegister(
 #   first_name="Ayla",
  #  last_name="Smith",
  #  username="ayla_new",  # change this
  #  phone_number="1234567890",
  #  gender="Female",
   # password="pass123",
   # confirm_password="pass123"
#)
#manager.register_manager()

# ----- Test Player Manager -----
# print("\n--- Adding Player ---")
# player_manager = PlayerManager()
#
# print("for Galatasary team")
# player_manager.add_player(1, "Fernando Muslera", "Galatasaray", "Goalkeeper")
# player_manager.add_player(24, "Elias Jelert", "Galatasaray", "Right back")
# player_manager.add_player(6, "Davinson Sánchez", "Galatasaray", "Centre back")
# player_manager.add_player(42, "Abdülkerim Bardakcı", "Galatasaray", "Centre back")
# player_manager.add_player(4, "Ismail Jakobs", "Galatasaray", "Left back")
# player_manager.add_player(23, "Kaan Ayhan", "Galatasaray", "Defensive midfielder")
# player_manager.add_player(8, "Lucas Torreira", "Galatasaray", "Central midfielder")
# player_manager.add_player(10, "Dries Mertens", "Galatasaray", "Attacking midfielder")
# player_manager.add_player(7, "Kerem Aktürkoğlu", "Galatasaray", "Right winger")
# player_manager.add_player(9, "Mauro Icardi", "Galatasaray", "Striker")
# player_manager.add_player(11, "Wilfried Zaha", "Galatasaray", "Left winger")
#
# print("for Beşiktaş team")
# player_manager.add_player(34, "Mert Günok", "Beşiktaş", "Goalkeeper")
# player_manager.add_player(2, "Valentin Rosier", "Beşiktaş", "Right back")
# player_manager.add_player(4, "Omar Colley", "Beşiktaş", "Centre back")
# player_manager.add_player(5, "Necip Uysal", "Beşiktaş", "Centre back")
# player_manager.add_player(3, "Arthur Masuaku", "Beşiktaş", "Left back")
# player_manager.add_player(6, "Salih Uçan", "Beşiktaş", "Defensive midfielder")
# player_manager.add_player(8, "Gedson Fernandes", "Beşiktaş", "Central midfielder")
# player_manager.add_player(10, "Rachid Ghezzal", "Beşiktaş", "Attacking midfielder")
# player_manager.add_player(7, "Cenk Tosun", "Beşiktaş", "Right winger")
# player_manager.add_player(9, "Vincent Aboubakar", "Beşiktaş", "Striker")
# player_manager.add_player(11, "Jackson Muleka", "Beşiktaş", "Left winger")
#
# print("for FC Barcelona team")
# player_manager.add_player(13, "Iñaki Peña", "FC Barcelona", "Goalkeeper")
# player_manager.add_player(23, "Jules Koundé", "FC Barcelona", "Right back")
# player_manager.add_player(4, "Ronald Araújo", "FC Barcelona", "Centre back")
# player_manager.add_player(33, "Pau Cubarsí", "FC Barcelona", "Centre back")
# player_manager.add_player(28, "Alejandro Balde", "FC Barcelona", "Left back")
# player_manager.add_player(6, "Gavi", "FC Barcelona", "Central midfielder")
# player_manager.add_player(8, "Pedri", "FC Barcelona", "Central midfielder")
# player_manager.add_player(16, "Fermín López", "FC Barcelona", "Attacking midfielder")
# player_manager.add_player(27, "Lamine Yamal", "FC Barcelona", "Right winger")
# player_manager.add_player(9, "Robert Lewandowski", "FC Barcelona", "Striker")
# player_manager.add_player(11, "Raphinha", "FC Barcelona", "Left winger")
#
# print("for Real Madrid team")
# player_manager.add_player(1, "Thibaut Courtois", "Real Madrid", "Goalkeeper")
# player_manager.add_player(2, "Dani Carvajal", "Real Madrid", "Right back")
# player_manager.add_player(3, "Éder Militão", "Real Madrid", "Centre back")
# player_manager.add_player(22, "Antonio Rüdiger", "Real Madrid", "Centre back")
# player_manager.add_player(23, "Ferland Mendy", "Real Madrid", "Left back")
# player_manager.add_player(18, "Aurélien Tchouaméni", "Real Madrid", "Defensive midfielder")
# player_manager.add_player(15, "Federico Valverde", "Real Madrid", "Central midfielder")
# player_manager.add_player(5, "Jude Bellingham", "Real Madrid", "Attacking midfielder")
# player_manager.add_player(11, "Rodrygo", "Real Madrid", "Right winger")
# player_manager.add_player(7, "Vinícius Júnior", "Real Madrid", "Left winger")
# player_manager.add_player(10, "Kylian Mbappé", "Real Madrid", "Striker")
#
# print("for manchester city team")
# #i did not add the substitutes
# player_manager.add_player(31, "Ederson", "Manchester City", "Goalkeeper")
# player_manager.add_player(2, "Kyle Walker", "Manchester City", "Right back")
# player_manager.add_player(3, "Ruben Dias", "Manchester City", "Centre back")
# player_manager.add_player(5, "John Stones", "Manchester City", "Centre back")
# player_manager.add_player(24, "Joško Gvardiol", "Manchester City", "Left back")
# player_manager.add_player(16, "Rodri", "Manchester City", "Defensive midfielder")
# player_manager.add_player(17, "Kevin De Bruyne", "Manchester City", "Central midfielder")
# player_manager.add_player(20, "Bernardo Silva", "Manchester City", "Attacking midfielder")
# player_manager.add_player(47, "Phil Foden", "Manchester City", "Right winger")
# player_manager.add_player(10, "Jack Grealish", "Manchester City", "Left winger")
# player_manager.add_player(9, "Erling Haaland", "Manchester City", "Striker")
#
# print("for manchester united team")
# #did not add the substitutes
# player_manager.add_player(24, "Andre Onana", "Manchester United", "Goalkeeper")
# player_manager.add_player(20, "Diogo Delot", "Manchester United", "Right back")
# player_manager.add_player(4, "Matthijs de Ligt", "Manchester United", "Centre back")
# player_manager.add_player(6, "Lisandro Martinez", "Manchester United", "Centre back")
# player_manager.add_player(23, "Luke Shaw", "Manchester United", "Left back")
# player_manager.add_player(18, "Casemiro", "Manchester United", "Defensive midfielder")
# player_manager.add_player(8, "Bruno Fernandes", "Manchester United", "Attacking midfielder")
# player_manager.add_player(7, "Mason Mount", "Manchester United", "Central midfielder")
# player_manager.add_player(17, "Alejandro Garnacho", "Manchester United", "Right winger")
# player_manager.add_player(10, "MArcus Rashford", "Manchester United", "Left winger")
# player_manager.add_player(9, "Joshua Zirkzee", "Manchester United", "Striker")
#
# print("for Al Wahda team")
# player_manager.add_player(1, "Ahmad Madania", "Al Wahda", "Goalkeeper")
# player_manager.add_player(2, "Moayad Ajan", "Al Wahda", "Left back")
# player_manager.add_player(3, "Abdulkader Dakka", "Al Wahda", "Centre back")
# player_manager.add_player(4, "Amro Jenyat", "Al Wahda", "Right back")
# player_manager.add_player(5, "Khaled Kurdaghli", "Al Wahda", "Centre back")
# player_manager.add_player(6, "Ahmad Al-Ashqar", "Al Wahda", "Central midfielder")
# player_manager.add_player(7, "Mahmoud Al Aswad", "Al Wahda", "Central midfielder")
# player_manager.add_player(8, "Zakariya Hanan", "Al Wahda", "Attacking midfielder")
# player_manager.add_player(9, "Mohammad Al-Hallaq", "Al Wahda", "Right winger")
# player_manager.add_player(10, "Mardik Mardikian", "Al Wahda", "Left winger")
# player_manager.add_player(11, "Omar Khribin", "Al Wahda", "Striker")
#
# print("for Al Karamah team")
# player_manager.add_player(1, "Shahir Al-Shaker", "Al Karamah", "Goalkeeper")
# player_manager.add_player(2, "Abdullah Al Shami", "Al Karamah", "Centre back")
# player_manager.add_player(3, "Ward Salama", "Al Karamah", "Central midfielder")
# player_manager.add_player(4, "Nasouh Al Nakdali", "Al Karamah", "Striker")
# player_manager.add_player(5, "Mohammad Al Marmour", "Al Karamah", "Left winger")
# player_manager.add_player(6, "Yousef Kalfa", "Al-Karamah", "Right winger")
# player_manager.add_player(7, "Tamer Haj Mohamad", "Al Karamah", "Defensive midfielder")
# player_manager.add_player(8, "Mohammad Fares", "Al Karamah", "Right back")
# player_manager.add_player(9, "Anas Balhous", "Al Karamah", "Left back")
# player_manager.add_player(10, "Abdul Malek Anbar", "Al Karamah", "Centre back")
# player_manager.add_player(11, "Mohammad Al Wakid", "Al Karamah", "Attacking midfielder")
#
# print("for Fenerbahçe team")
# player_manager.add_player(40, "Dominik Livakovic", "Fenerbahçe", "Goalkeeper")
# player_manager.add_player(21, "Bright Osayi-Samuel", "Fenerbahçe", "Right back")
# player_manager.add_player(6, "Alexander Djiku", "Fenerbahçe", "Centre back")
# player_manager.add_player(4, "Çağlar Söyüncü", "Fenerbahçe", "Centre back")
# player_manager.add_player(7, "Ferdi Kadıoğlu", "Fenerbahçe", "Left back")
# player_manager.add_player(35, "Fred", "Fenerbahçe", "Midfielder")
# player_manager.add_player(17, "İrfan Can Kahveci", "Fenerbahçe", "Central midfielder")
# player_manager.add_player(10, "Dusan Tadic", "Fenerbahçe", "Attacking midfielder")
# player_manager.add_player(20, "Allan Saint-Maximin", "Fenerbahçe", "Right winger")
# player_manager.add_player(9, "Youssef En-Nesyri", "Fenerbahçe", "Striker")
# player_manager.add_player(11, "Emre Mor", "Fenerbahçe", "Left winger")
#
# print("for Al Ahly team")
# #names done without substitutes
# player_manager.add_player(1,"Mohamed El Shenawy", "Al Ahly", "Goalkeeper")
# player_manager.add_player(30, "Mohamed Hany", "Al Ahly", "Right back")
# player_manager.add_player(6, "Yasser Ibrahim", "Al Ahly", "Centre back")
# player_manager.add_player(5, "Rami Rabia", "Al Ahly", "Centre back")
# player_manager.add_player(21, "Ali Maaloul", "Al Ahly", "Left back")
# player_manager.add_player(8, "Akram Tawfik", "Al Ahly", "Defensive midfielder")
# player_manager.add_player(13, "Marwan Attia", "Al Ahly", "Central midfielder")
# player_manager.add_player(22, "Emam Ashour", "Al Ahly", "Attacking midfielder")
# player_manager.add_player(14, "Hussein El Shahat", "Al Ahly", "Right winger")
# player_manager.add_player(12, "Reda Slim", "Al Ahly", "Left winger")
# player_manager.add_player(9, "Wessam Abou Ali", "Al Ahly", "Striker")
#
# print("for Zamalek team")
# #zamalak done without substitutes
# player_manager.add_player(1, "Mohamed Awad", "Zamalek", "Goalkeeper")
# player_manager.add_player(24, "Hamza Mathlouthi", "Zamalek", "Right back")
# player_manager.add_player(5, "Hossam Abdelmaguid", "Zamalek", "Centre back")
# player_manager.add_player(6, "Mostafa El Zenary", "Zamalek", "Centre back")
# player_manager.add_player(13,"Ahmed Abou El Fotouh", "Zamalek", "Left back")
# player_manager.add_player(8, "Nabil Dungar", "Zamalek", "Defensive midfielder")
# player_manager.add_player(12, "Seif Farouk Gaafar", "Zamalek", "Central midfielder")
# player_manager.add_player(14, "Ahmed Hamdi", "Zamalek", "Attacking midfielder")
# player_manager.add_player(25, "Ahmed Sayed", "Zamalek", "Right winger")
# player_manager.add_player(11, "Mostafa Shalaby", "Zamalek", "Left winger")
# player_manager.add_player(30, "Seifeddine Jaziri", "Zamalek", "Striker")
#
# # ----- Test Team Manager -----
# print("\n--- Adding Team ---")
# team_manager = TeamManager()
# team_manager.add_team(
#     team_name="Manchester City",
#     coach_name="Pep Guardiola",
#     team_country="ُEngland"
# )
# team_manager.add_team(
#     team_name="Manchester United ",
#     coach_name="Rúben Amorim",
#     team_country="England"
# )
# team_manager.add_team(
#     team_name="Al Wahda",
#     coach_name="Nizar Mahrous",
#     team_country="Syria"
# )
# team_manager.add_team(
#     team_name="AL Karamah",
#     coach_name="Muhammed Kuayd",
#     team_country="Syria"
# )
# team_manager.add_team(
#     team_name="Fenerbahçe",
#     coach_name="José Mourinho",
#     team_country="Türkiye"
# )
# team_manager.add_team(
#     team_name="Al Ahly",
#     coach_name="José Riveiro",
#     team_country="Egypt"
# )
# team_manager.add_team(
#     team_name="Zamalek",
#     coach_name="Christian Gross",
#     team_country="Türkiye"
# )


# ----- Test Match Manager -----
#we have 24 matches
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Beşiktaş",
#     team2_name="FC Barcelona",
#     match_date="2025-06-01",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Manchester City",
#     team2_name="Fenerbahçe",
#     match_date="2025-06-02",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="FC Barcelona",
#     team2_name="Zamalek",
#     match_date="2025-06-08",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Al-Karamah SC",
#     team2_name="Fenerbahçe",
#     match_date="2025-06-09",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Fenerbahçe",
#     team2_name="Zamalek",
#     match_date="2025-06-10",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="FC Barcelona",
#     team2_name="Al Ahly",
#     match_date="2025-06-15",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Fenerbahçe",
#     team2_name="Beşiktaş",
#     match_date="2025-06-16",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Galatasaray",
#     team2_name="Al Ahly",
#     match_date="2025-06-22",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Al-Karamah SC",
#     team2_name="Al Ahly",
#     match_date="2025-06-23",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Manchester City",
#     team2_name="FC Barcelona",
#     match_date="2025-06-24",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Manchester City",
#     team2_name="Zamalek",
#     match_date="2025-06-29",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Manchester United",
#     team2_name="FC Barcelona",
#     match_date="2025-06-30",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Real Madrid",
#     team2_name="Al Ahly",
#     match_date="2025-07-01",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Manchester United",
#     team2_name="Beşiktaş",
#     match_date="2025-07-06",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Manchester United",
#     team2_name="Galatasaray",
#     match_date="2025-07-07",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Real Madrid",
#     team2_name="Al Wahda SC",
#     match_date="2025-07-13",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Galatasaray",
#     team2_name="Zamalek",
#     match_date="2025-07-14",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Manchester City",
#     team2_name="Real Madrid",
#     match_date="2025-07-15",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Al Wahda SC",
#     team2_name="Beşiktaş",
#     match_date="2025-07-20",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Al Ahly",
#     team2_name="Zamalek",
#     match_date="2025-07-21",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Galatasaray",
#     team2_name="Al Wahda SC",
#     match_date="2025-07-22",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Manchester United",
#     team2_name="Real Madrid",
#     match_date="2025-07-27",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Manchester United",
#     team2_name="Zamalek",
#     match_date="2025-07-28",
#     score_team1=None,
#     score_team2=None
# )
#
# print("\n--- Adding Match ---")
# match_manager = MatchManager()
# match_manager.add_match(
#     team1_name="Al-Karamah SC",
#     team2_name="Manchester United",
#     match_date="2025-07-29",
#     score_team1=None,
#     score_team2=None
# )


