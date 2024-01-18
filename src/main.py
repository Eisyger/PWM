from register import Register
from login import Login
from cryptography import Cryptography
import os


class Main:
    def __init__(self):
        self.path = "save_file.mpw"
        self.salt = "1|<y18#+-.fvtvk.49610/*"
        self.pepper = "anti_rainbow"
        self.cypher = Cryptography(self.salt, self.pepper)

    def run(self):
        # when no password file exists, start register
        while not os.path.exists(self.path):
            register = Register(self.path, self.cypher)
            register.run()

        # when password file exits, start login
        login = Login(self.path, self.cypher)
        if login.run():
            print("juhu login erfolgreich!")
        else:
            print("Sorry Dude...")


if __name__ == "__main__":
    main = Main()
    main.run()
