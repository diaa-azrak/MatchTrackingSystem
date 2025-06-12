from db_connection import get_connection

def insert_test_card():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # بيانات البطاقة المراد إدخالها
        card_id = 1 # تأكدي أنه غير مستخدم مسبقاً
        player_id = 4
        match_id = 9
        card_type = "Yellow"

        insert_query = """
            INSERT INTO cards (card_id, player_id, match_id, card_type)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (card_id, player_id, match_id, card_type))

        conn.commit()
        print("Test card inserted successfully!")

    except Exception as e:
        print("Error inserting test card:", e)

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    insert_test_card()
