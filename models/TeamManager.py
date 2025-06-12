from db_connection import get_connection

class TeamManager:
    def fetch_teams(self):
        conn = get_connection()
        if not conn:
            return []

        cursor = conn.cursor()
        try:
            # Only select the existing columns
            cursor.execute("SELECT team_name, coach_name, team_country FROM teams ORDER BY team_name;")
            return cursor.fetchall()  # Returns list of tuples
        except Exception as e:
            print("DB error in fetch_teams:", e)
            return []
        finally:
            cursor.close()
            conn.close()

    # Add a new team
    def add_team(self, team_name, coach_name, team_country):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = """
            INSERT INTO teams (team_name, coach_name, team_country)
            VALUES (%s, %s, %s)
            """
            cursor.execute(query, (team_name, coach_name, team_country))
            conn.commit()
            print("Team added.")
        except Exception as e:
            print("Add team failed:", e)
        finally:
            cursor.close()
            conn.close()

    # Update an existing team
    def update_team(self, team_id, team_name=None, coach_name=None, team_country=None):
        conn = get_connection()
        cursor = conn.cursor()

        updates = []
        values = []

        if team_name:
            updates.append("team_name = %s")
            values.append(team_name)
        if coach_name:
            updates.append("coach_name = %s")
            values.append(coach_name)
        if team_country:
            updates.append("team_country = %s")
            values.append(team_country)

        if not updates:
            print("No update data provided.")
            return

        values.append(team_id)
        query = f"UPDATE teams SET {', '.join(updates)} WHERE team_id = %s"

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Team updated.")
        except Exception as e:
            print("Update failed:", e)
        finally:
            cursor.close()
            conn.close()

    # Delete a team by ID
    def delete_team(self, team_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM teams WHERE team_id = %s", (team_id,))
            conn.commit()
            print("Team deleted.")
        except Exception as e:
            print("Delete failed:", e)
        finally:
            cursor.close()
            conn.close()