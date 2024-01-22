from crypto import Cryptography
from load import Load
from pwinput import PWInput
import hashlib
import base64
import sys


class Login(PWInput):
    def __init__(self, path: str, cypher: Cryptography, max_login_fails: int = 5):
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
                hashed_data = self.cypher.encrypt_and_hash(data)

                # get hash from file
                hashed_pw = Load.load_file(self.path)

                # compare hashes
                if hashed_data == hashed_pw:
                    print("Login erfolgreich.")
                    print("----------------------------------------------")
                    return True
                else:
                    print("##############################################")
                    print("Falscher Benutzer oder falsches Passwort.")
                    print("Versuche es erneut.")
                    print("##############################################")
                    fail_counter += 1

        # when to many logins faild close
        if fail_counter == self.max_login_fails:
            sys.exit(1)

        return False

    def get_key(self):
        seed = self.password + self.username
        key_bytes = hashlib.sha256(seed.encode('utf-8')).digest()
        base64_key = base64.urlsafe_b64encode(key_bytes)
        return base64_key
