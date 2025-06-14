from db_connection import get_connection

class RegisterHandler:
    def __init__(self, first_name, last_name, username, phone_number, gender, password, confirm_password, role):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone_number = phone_number
        self.gender = gender
        self.password = password
        self.confirm_password = confirm_password
        self.role = role  # يجب أن تكون "Manager" أو "User"

    def register(self):
        # تأكد من تطابق كلمة المرور
        if self.password != self.confirm_password:
            return False, "Passwords do not match."

        if self.role not in ["Manager", "User"]:
            return False, "Invalid role. Must be 'Manager' or 'User'."

        table_name = "register_manager" if self.role == "Manager" else "register_user"

        conn = get_connection()
        if not conn:
            return False, "Database connection failed."

        cursor = conn.cursor()
        query = f"""
            INSERT INTO {table_name}
            (first_name, last_name, username, phone_number, gender, password)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            self.first_name,
            self.last_name,
            self.username,
            self.phone_number,
            self.gender,
            self.password  # من الأفضل استخدام تشفير حقيقي لكلمة المرور
        )

        try:
            cursor.execute(query, values)
            conn.commit()
            return True, f"{self.role} registered successfully."
        except Exception as e:
            return False, f"Registration failed: {str(e)}"
        finally:
            cursor.close()
            conn.close()
