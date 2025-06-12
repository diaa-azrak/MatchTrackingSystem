from db_connection import get_connection

class MatchManager:
    # Add a new match
    def add_match(self, team1_name, team2_name, match_date, score_team1, score_team2):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = """
            INSERT INTO matchs (team1_name, team2_name, match_date, score_team1, score_team2)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (team1_name, team2_name, match_date, score_team1, score_team2))
            conn.commit()
            print("Match added.")
        except Exception as e:
            print("Add match failed:", e)
        finally:
            cursor.close()
            conn.close()

    # Update match scores or date
    def update_match(self, id, team1_name=None, team2_name=None, match_date=None, score_team1=None, score_team2=None):
        conn = get_connection()
        cursor = conn.cursor()

        updates = []
        values = []

        if team1_name:
            updates.append("team1_name = %s")
            values.append(team1_name)
        if team2_name:
            updates.append("team2_name = %s")
            values.append(team2_name)
        if match_date:
            updates.append("match_date = %s")
            values.append(match_date)
        if score_team1 is not None:
            updates.append("score_team1 = %s")
            values.append(score_team1)
        if score_team2 is not None:
            updates.append("score_team2 = %s")
            values.append(score_team2)

        if not updates:
            print("No data provided to update.")
            return

        values.append(match_id)
        query = f"UPDATE matchs SET {', '.join(updates)} WHERE id = %s"

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Match updated.")
        except Exception as e:
            print("Update failed:", e)
        finally:
            cursor.close()
            conn.close()

    # Delete a match
    def delete_match(self, match_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM matchs WHERE match_id = %s", (match_id,))
            conn.commit()
            print("Match deleted.")
        except Exception as e:
            print("Delete failed:", e)
        finally:
            cursor.close()
            conn.close()

    def get_all_matches(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, team1_name, team2_name, match_date, score_team1, score_team2 FROM matchs"
            )
            return cursor.fetchall()
        except Exception as e:
            print("DB error in get_all_matches:", e)
            return []
        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass
