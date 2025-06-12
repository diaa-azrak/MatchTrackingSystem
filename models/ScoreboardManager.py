from db_connection import get_connection

class ScoreboardManager:
    def fetch_scoreboard(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)  # so it returns results as dictionaries

        query = """
        SELECT 
            team_name,
            COUNT(*) AS matches_played,
            SUM(CASE 
                WHEN (score_team1 > score_team2 AND team1_name = team_name) OR 
                     (score_team2 > score_team1 AND team2_name = team_name)
                THEN 1 ELSE 0 END) AS wins,
            SUM(CASE 
                WHEN score_team1 = score_team2 THEN 1 ELSE 0 END) AS draws,
            SUM(CASE 
                WHEN (score_team1 < score_team2 AND team1_name = team_name) OR 
                     (score_team2 < score_team1 AND team2_name = team_name)
                THEN 1 ELSE 0 END) AS losses,
            SUM(
                CASE 
                    WHEN (score_team1 > score_team2 AND team1_name = team_name) OR 
                         (score_team2 > score_team1 AND team2_name = team_name)
                    THEN 3
                    WHEN score_team1 = score_team2 THEN 1
                    ELSE 0
                END
            ) AS points
                FROM (
            SELECT team1_name AS team_name, team1_name, team2_name, score_team1, score_team2 FROM matchs
            UNION ALL
            SELECT team2_name AS team_name, team1_name, team2_name, score_team2 AS score_team1, score_team1 AS score_team2 FROM matchs
        ) AS all_matches
        GROUP BY team_name
        ORDER BY points DESC
        """

        try:
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print("Error fetching scoreboard:", e)
            return []
        finally:
            cursor.close()
            conn.close()