from restrictions import Restrictions
from cryptography import Cryptography
from save import Save

import getpass


class Register:
    def __init__(self, path: str, cypher: Cryptography):
        self.path = path
        self.cypher = cypher
        self.username = ""
        self.password = ""

    def run(self):
        print("REGISTER")
        try:
            if self.user_input():
                if self.password_input():
                    data = [self.username, self.password]
                    if Save.encrypt_and_save_file(self.path, self.cypher, data):
                        print("Masterpasswort erfolgreich gespeichert.")
                        print("Merke dir das Passwort oder bewahre es sicher auf.")
                        print("NICHT DIGITAL!")
        except Exception as e:
            print(e)
            raise SystemExit("Programm wird beendet.")

    def user_input(self):
        while True:
            user = input("Eingabe Username: ")
            if Restrictions.check_username(user):
                self.username = user
                return True
            else:
                continue

    def password_input(self):
        while True:
            pw = getpass.getpass(prompt="Eingabe Passwort: ")
            if Restrictions.check_password(pw):
                self.password = pw
                if self.verify_password():
                    return True

    def verify_password(self):
        pw = getpass.getpass(prompt="Eingabe Passwort Wiederholung: ")
        if self.password == pw:
            return True
        return False
