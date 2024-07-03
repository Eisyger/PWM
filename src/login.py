from crypto import Crypto
from load import Load
from pwinput import PWInput
import sys


class Login(PWInput):
    def __init__(self, path: str, cypher: Crypto):
        super().__init__()
        self.path = path
        self.cypher = cypher

    def run(self, start_text: str = "LOGIN", max_login_fails: int = 3) -> bool:
        """
        Runs the Login query on Console. When '`max_login_fails`' is reached, exit the application.

        Args:
            start_text (str, optional): The text to display at the beginning of the login process. Defaults to "LOGIN".
            max_login_fails (int, optional): The maximum number of login failures allowed before exiting the application.
            Defaults to 3.

        Returns:
            bool: True if login is successful, False otherwise.
        """

        # count login fails, and exit
        fail_counter = 0
        while fail_counter < max_login_fails:

            # get userinput for username and password
            if super().run(start_text):
                
                # get salt and hashed masterpassword from file
                hashed_data = Load.load_password(self.path)
                salt = hashed_data[0]
                hashed_pw = hashed_data[1]

                # generate data list from userinput and hash it
                data = [salt, self.username, self.password]
                # generate hash - have to add the new line, because the masterpassword is save so too
                new_hashed_data = self.cypher.encrypt_password(data) + "\n"
                

                # compare hashes
                if new_hashed_data == hashed_data:
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
            else:
                fail_counter += 1

        # when to many login fails, close application
        if fail_counter >= max_login_fails:
            sys.exit(1)
        return False

    def get_key(self) -> bytes:

        """Returns a base64 key for encoding the database."""

        seed = self.password + self.username
        return Crypto.generate_fenet_key(seed)


