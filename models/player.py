from db_connection import get_connection

class Player:
    def __init__(self, player_name, team_name, player_position):
        self.player_name = player_name
        self.team_name = team_name
        self.player_position = player_position

    def save_to_db(self):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO players (player_name, team_name, player_position)
        VALUES (%s, %s, %s)
        """
        values = (self.player_name, self.team_name, self.player_position)

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Player saved successfully")
        except Exception as e:
            print("Player save failed", e)
        finally:
            cursor.close()
            conn.close()