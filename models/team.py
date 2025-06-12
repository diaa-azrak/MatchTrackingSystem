from db_connection import get_connection

class Team:
    def __init__(self, team_name, coach_name):
        self.team_name = team_name
        self.coach_name = coach_name

    def save_to_db(self):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO teams (team_name, coach_name)
        VALUES (%s, %s)
        """
        values = (self.team_name, self.coach_name)

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Team saved successfully!")
        except Exception as e:
            print("Team save failed:", e)
        finally:
            cursor.close()
            conn.close()