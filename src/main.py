from register import Register
from login import Login
from crypto import Cryptography
from account_manager import AccountManager
import os


class Main:
    def __init__(self):
        self.path_mpw = "save_file.mpw"
        self.path_data = "save_file_data.mpw"
        self.salt = "1|<y18#+-.fvtvk.49610/*"
        self.pepper = "anti_rainbow"
        self.cypher = Cryptography(self.salt, self.pepper)

    def run(self):
        # when no master password file exists, start register and generate one
        while not os.path.exists(self.path_mpw):
            # start Register
            register = Register(self.path_mpw, self.cypher)
            register.run()

        # when password file exits, start login
        login = Login(self.path_mpw, self.cypher)
        if login.run():
            # get key from login data, to encrypt the save files
            auth_key = login.get_key()

            # start the AccountManager
            account_manager = AccountManager(self.path_data, auth_key)
            account_manager.run()


if __name__ == "__main__":
    main = Main()
    main.run()
