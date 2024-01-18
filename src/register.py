from restrictions import Restrictions
from cryptography import Cryptography
from pwinput import PWInput
from save import Save

import getpass


class Register(PWInput):
    def __init__(self, path: str, cypher: Cryptography):
        super().__init__()
        self.path = path
        self.cypher = cypher        

    def run(self):
        try:
            if super().run("REGISTER"):
                if self.verify_password():
                    data = [self.username, self.password]
                    if Save.encrypt_and_save_file(self.path, self.cypher, data):
                        print("Masterpasswort erfolgreich gespeichert.")
                        print("Merke dir das Passwort oder bewahre es sicher auf.")
                        print("NICHT DIGITAL!")
        except Exception as e:
            print(e)
            raise SystemExit("Programm wird beendet.")
    

    def verify_password(self):
        pw = getpass.getpass(prompt="Eingabe Passwort Wiederholung: ")
        if self.password == pw:
            return True
        return False
