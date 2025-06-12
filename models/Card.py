from db_connection import get_connection

class CardManager:
    def get_all_cards(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = '''
            SELECT 
                cards.card_id,
                players.player_id,
                players.player_name,
                teams.team_name,
                matches.match_id,
                cards.card_type
            FROM 
                cards
            JOIN players ON cards.player_id = players.player_id
            JOIN teams ON players.team_id = teams.team_id
            JOIN matches ON cards.match_id = matches.match_id
            ORDER BY cards.card_id
            '''
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print("Error fetching cards:", e)
            return []
        finally:
            cursor.close()
            conn.close()
