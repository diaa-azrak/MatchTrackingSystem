from models.LoginHandler import ManagerLogin

username = input("Enter username: ")
password = input("Enter password: ")

login = ManagerLogin(username, password)
login.login()