from register import Register
from login import Login
from crypto import Crypto
from account_manager import AccountManager
import os


class Main:
    def __init__(self):
        self.path_mpw = "save_file.mpw"
        self.path_data = "save_file_data.mpw"
        self.salt = "1|<y18#+-.fvtvk.49610/*"
        self.pepper = "anti_rainbow"
        self.cypher = Crypto(self.salt, self.pepper)

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

            # start the DBManager
            """TODO implement data management, decrypt data from file fails."""
            db_manager = AccountManager(self.path_data, auth_key)
            db_manager.print_data(all=True)
            while True:
                eingabe = input().split(' ')
                if eingabe[0] == "exit":
                    print("Beende den Passwort Manager.")
                    print("Änderungen speichern? Y/N")
                    if input() == "Y":
                        db_manager.save()
                    break
                elif eingabe[0] == "help":
                    if len(eingabe) == 1:
                        print("exit \t Beendet den Passwort Manager.")
                        print("print \t Gib alle Accounts in Kurzform aus.")
                        print("print -l \t Gib alle Accounts in Langform aus.")
                        print("print ACCOUNT_NAME \t Gib den genannten Account aus.")
                        print("get ACCOUNT_NAME \t Fügt das Passwort in den Zwischespeicher ein.")
                        print("remove ACCOUNT_NAME \t Löscht den Account.")

                elif eingabe[0] == "print":
                    if len(eingabe) == 1:
                        db_manager.print_data(all=True, short=True)
                        continue
                    if len(eingabe) == 2:
                        if eingabe[1] == "-l":
                            db_manager.print_data(all=True, short=False)
                            continue
                        elif eingabe[1]:
                            db_manager.print_data(name=eingabe[1])

                elif eingabe[0] == "get":
                    if len(eingabe) == 2:
                        db_manager.get_password(eingabe[1])
                        continue

                elif eingabe[0] == "remove":
                    if len(eingabe) == 2:
                        db_manager.remove(eingabe[1])
                        continue
                print("Eingabe ungültig, schreibe 'help' für Hilfe.")



if __name__ == "__main__":
    main = Main()
    main.run()
