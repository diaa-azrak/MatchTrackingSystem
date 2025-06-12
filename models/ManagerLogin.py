from db_connection import get_connection

class ManagerLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT password FROM register_manager WHERE username = %s", (self.username,))
            result = cursor.fetchone()

            if result:
                stored_password = result[0]
                if self.password == stored_password:
                    print("Login Successful")
                    return True
                else:
                    print("Incorrect Password")
                    return False

            else:
                print("Username not found")
                return False
        except Exception as e:
            print("Login Failed:", e)
            return False
        finally:
            cursor.close()
            conn.close()