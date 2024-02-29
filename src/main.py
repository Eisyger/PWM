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
            db_manager = AccountManager(self.path_data, auth_key)
            db_manager.print_data(all=True)
            while True:
                eingabe = input("->").split(' ')

                if eingabe[0] == "exit":
                    print("Beende den Passwort Manager.")
                    abfrage = input("Änderungen speichern? Y/N: ")
                    if abfrage.lower() == "y":
                        db_manager.save()
                        print("Änderungen gespeichert.")
                    else:
                        print("Änderungen wurden nicht gespeichert.")
                    break

                elif eingabe[0] == "help":
                    if len(eingabe) == 1:
                        print("p                    \t Gib alle Accounts in Kurzform aus.")
                        print("p -l                 \t Gib alle Accounts in Langform aus.")
                        print("p ACCOUNT_NAME       \t Gib die Account Daten aus.")
                        print("get ACCOUNT_NAME     \t Fügt das Passwort in den Zwischespeicher ein.")
                        print("add                  \t Erzeuge neuen Account.")
                        print("edit                 \t Editiere einen Account.")
                        print("remove ACCOUNT_NAME  \t Löscht den Account.")
                        print("clear                \t Bereinige die Console.")
                        print("exit                 \t Speichern und Beenden.")
                        print("Das Passwort wird nicht in lesbarer Form ausgegeben. "
                              "Verwende den Befehl 'get ACCOUNT_NAME um das Passwort des gesuchten "
                              "Accounts in die Zwischenablage zu speichern.")
                        continue

                elif eingabe[0] == "p":
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

                elif eingabe[0] == "add":
                    if len(eingabe) == 1:
                        db_manager.add()
                        continue

                elif eingabe[0] == "edit":
                    acc_name = input("Gib den Account Namen ein: ")
                    db_manager.print_data(acc_name, short=False)
                    field = input("Feld, z.B. password: ").lower()
                    changes = input(f"Neue Eingabe für den Account {acc_name} in {field}: ")
                    if acc_name and field and changes:
                        db_manager.edit(acc_name, field, changes)
                        continue
                    else:
                        print("Ungültige Eingabe.")
                        continue

                elif eingabe[0] == "clear":
                    if len(eingabe) == 1:
                        os.system('cls' if os.name == 'nt' else 'clear')
# TODO der Manager ist soweit fertig. Es wäre noch eine Passwort ändern Möglichkeit gut.
                print("Eingabe ungültig, schreibe 'help' für Hilfe.")
        else:
            print("Falsches Passwort. Beende Passwort Manager.")


if __name__ == "__main__":
    main = Main()
    main.run()
