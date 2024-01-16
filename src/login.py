from cryptography import Cryptography
from load import Load
import getpass

class Login:
    def __init__(self, path: str, cypher: Cryptography):
        self.path = path
        self.cypher = cypher
        self.username = ""
        self.password = ""

    def run(self):
        print("LOGIN")
        try:
            while True:
                user = input("Eingabe Username: ")
                pw = getpass.getpass(prompt="Eingabe Passwort: ")
                data = Load.load_and_decrypt_file(self.path, self.cypher)
                """TODO extra Methode für die cypher instanz zum verifizieren der daten"""
                print(data)

        except Exception as e:
            print(e)
            raise SystemExit("Programm wird beendet.")

