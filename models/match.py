from db_connection import get_connection

class Match:
    def __init__(self, team1_name, team2_name, match_date, score_team1, score_team2):
        self.team1_name = team1_name
        self.team2_name = team2_name
        self.match_date = match_date
        self.score_team1 = score_team1
        self.score_team2 = score_team2

    def save_to_db(self):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO matchs (team1_name, team2_name, match_date, score_team1, score_team2)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            self.team1_name,
            self.team2_name,
            self.match_date,
            self.score_team1,
            self.score_team2
        )

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Match saved successfully")
        except Exception as e:
            print("Match save failed:", e)
        finally:
            cursor.close()
            conn.close()