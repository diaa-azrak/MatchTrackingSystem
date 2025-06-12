from db_connection import get_connection

class PlayerManager:
    # Add a new player
    def add_player(self, player_id, name, team_name, position):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO players (player_id, player_name, team_name, player_position)
        VALUES (%s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (player_id, name, team_name, position))
            conn.commit()
            print("Player added.")
        except Exception as e:
            print("Add player failed:", e)
        finally:
            cursor.close()
            conn.close()

    # Update an existing player's data
    def update_player(self, player_id, name=None, team_name=None, position=None):
        conn = get_connection()
        cursor = conn.cursor()

        updates = []
        values = []

        if name:
            updates.append("player_name = %s")
            values.append(name)
        if team_name:
            updates.append("team_name = %s")
            values.append(team_name)
        if position:
            updates.append("player_position = %s")
            values.append(position)

        values.append(player_id)
        query = f"UPDATE players SET {', '.join(updates)} WHERE player_id = %s"

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Player updated.")
        except Exception as e:
            print("Update failed:", e)
        finally:
            cursor.close()
            conn.close()

    # Delete a player by ID
    def delete_player(self, player_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM players WHERE player_id = %s", (player_id,))
            conn.commit()
            print("Player deleted.")
        except Exception as e:
            print("Delete failed:", e)
        finally:
            cursor.close()
            conn.close()

    def get_all_players(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT player_id, player_name, team_name, player_position FROM players")
            results = cursor.fetchall()
            return results
        except Exception as e:
            print("Failed to fetch players:", e)
            return []
        finally:
            cursor.close()
            conn.close()