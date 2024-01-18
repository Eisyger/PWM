import getpass
from restrictions import Restrictions


class PWInput:
    def __init__(self):
        self.username = ""
        self.password = ""

    def run(self, start_text="") -> bool:
        print(start_text)
        if self.user_input():
            if self.password_input():
                return True

    def user_input(self) -> bool:
        while True:
            user = input("Eingabe Username: ")
            if Restrictions.check_username(user):
                self.username = user
                return True

    def password_input(self) -> bool:
        while True:
            pw = getpass.getpass(prompt="Eingabe Passwort: ")
            if Restrictions.check_password(pw):
                self.password = pw
                return True
