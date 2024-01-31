from crypto import Crypto
from pwinput import PWInput
from save import Save
import getpass


class Register(PWInput):
    def __init__(self, path: str, cypher: Crypto):
        super().__init__()
        self.path = path
        self.cypher = cypher

    def run(self, start_text="") -> bool:
        while True:
            # get userinput for username and password
            if super().run("REGISTER"):

                # enter password a second time
                if self.confirm_password():

                    # generate data, encrypt and save
                    data = [self.username, self.password]
                    if Save.save_password(self.path, self.cypher, data):
                        print("-" * 50)
                        print("Masterpasswort erfolgreich gespeichert.")
                        print("Merke dir das Passwort oder bewahre es sicher auf.")
                        print("NICHT DIGITAL!")
                        print("-" * 50)
                        return True

                else:
                    print("#" * 50)
                    print("Fehler! Die Passwörter stimmen nicht überein.")
                    print("Erneute Eingabe erfoderlich.")
                    print("#" * 50)

    def confirm_password(self):
        pw = getpass.getpass(prompt="Eingabe Passwort Wiederholung: ")
        if self.password == pw:
            return True
        return False
