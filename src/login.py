from crypto import Crypto
from load import Load
from pwinput import PWInput
import sys


class Login(PWInput):
    def __init__(self, path: str, cypher: Crypto, max_login_fails: int = 5):
        super().__init__()
        self.path = path
        self.cypher = cypher
        self.max_login_fails = max_login_fails

    def run(self, start_text: str = "") -> bool:
        # count login fails, and exit
        fail_counter = 0
        while fail_counter < self.max_login_fails:

            # get userinput for username and password
            if super().run("LOGIN"):

                # generate data list and hash it
                data = [self.username, self.password]
                hashed_data = self.cypher.encrypt_password(data)

                # get hash from file
                hashed_pw = Load.load_file(self.path)

                # compare hashes
                if hashed_data == hashed_pw:
                    print("-" * 50)
                    print("Login erfolgreich.")
                    print("-" * 50)
                    return True
                else:
                    print("#" * 50)
                    print("Falscher Benutzer oder falsches Passwort.")
                    print("Versuche es erneut.")
                    print("#" * 50)
                    fail_counter += 1

        # when to many logins faild close
        if fail_counter == self.max_login_fails:
            sys.exit(1)

        return False

    def get_key(self):
        seed = self.password + self.username
        return Crypto.generate_fenet_key(seed)


