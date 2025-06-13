# this class will store the username when logged in.
# showing other pages who is logged in.
# clearing the session when logging out
class SessionManager:
    logged_in_manager = None

    @classmethod
    def set_logged_in_manager(cls, username):
        cls.logged_in_manager = username

    @classmethod
    def get_logged_in_manager(cls):
        return cls.logged_in_manager

    @classmethod
    def clear_session(cls):
        cls.logged_in_manger = None