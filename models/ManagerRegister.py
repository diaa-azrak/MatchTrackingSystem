from db_connection import get_connection

class ManagerRegister:
    def __init__(self, first_name, last_name, username, phone_number, gender, password, confirm_password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone_number = phone_number
        self.gender = gender
        self.password = password
        self.confirm_password = confirm_password

    def register_manager(self):
        # Password confirmation check
        if self.password != self.confirm_password:
            print("Passwords do not match.")
            return

        conn = get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO register_manager 
            (first_name, last_name, username, phone_number, gender, password)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            self.first_name,
            self.last_name,
            self.username,
            self.phone_number,
            self.gender,
            self.password  # You can hash it for security in real projects
        )

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Manager registered successfully.")
        except Exception as e:
            print("Manager registration failed:", e)
        finally:
            cursor.close()
            conn.close()
