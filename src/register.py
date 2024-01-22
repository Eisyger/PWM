from crypto import Cryptography
from pwinput import PWInput
from save import Save
import getpass


class Register(PWInput):
    def __init__(self, path: str, cypher: Cryptography):
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
                    if Save.encrypt_and_save(self.path, self.cypher, data):
                        print("Masterpasswort erfolgreich gespeichert.")
                        print("Merke dir das Passwort oder bewahre es sicher auf.")
                        print("NICHT DIGITAL!")
                        return True

                else:
                    print("Fehler! Die Passwörter stimmen nicht überein.")
                    print("Erneute Eingabe erfoderlich.")
                    return False

    def confirm_password(self):
        pw = getpass.getpass(prompt="Eingabe Passwort Wiederholung: ")
        if self.password == pw:
            return True
        return False
