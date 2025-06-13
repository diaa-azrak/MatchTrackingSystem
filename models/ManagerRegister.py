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
        # تأكد من تطابق كلمة المرور
        if self.password != self.confirm_password:
            return False, "Passwords do not match."

        conn = get_connection()
        if not conn:
            return False, "Database connection failed."

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
            self.password
        )

        try:
            cursor.execute(query, values)
            conn.commit()
            return True, "Manager registered successfully."
        except Exception as e:
            return False, f"Registration failed: {str(e)}"
        finally:
            cursor.close()
            conn.close()
