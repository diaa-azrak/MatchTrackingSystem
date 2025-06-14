from db_connection import get_connection

class LoginHandler:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role  # "Manager" or "User"

    def login(self):
        table = "register_manager" if self.role == "Manager" else "register_user"

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(f"SELECT password FROM {table} WHERE username = %s", (self.username,))
            result = cursor.fetchone()
            cursor.close()
            conn.close()

            if result:
                stored_password = result[0]
                if self.password == stored_password:
                    return True, f"{self.role} login successful."
                else:
                    return False, "Incorrect password."
            else:
                return False, "Username not found."

        except Exception as e:
            return False, f"Login error: {str(e)}"

    def get_role(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT 1 FROM register_manager WHERE username = %s", (self.username,))
            if cursor.fetchone():
                return "Manager"

            cursor.execute("SELECT 1 FROM register_user WHERE username = %s", (self.username,))
            if cursor.fetchone():
                return "User"

            return "Unknown"
        except Exception as e:
            print("Role check error:", e)
            return "Unknown"
        finally:
            cursor.close()
            conn.close()
