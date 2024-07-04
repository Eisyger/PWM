from register import Register
from login import Login
from crypto import Crypto
from account_manager import AccountManager
import argparse
import os


class Main:
    def __init__(self, save_path: str = ""):
        self.path_database = os.path.join(save_path, "database.mpw")
        
        self.pepper = "anti_rainbow"
        self.cypher = Crypto(self.pepper)

    def run(self):
        # when no database file exists, start register and generate one
        if not os.path.exists(self.path_database):
            # start Register
            register = Register(self.path_database, self.cypher)
            register.run()

        # when database file exits, start login
        login = Login(self.path_database, self.cypher)
        if login.run():
            # get key from login data, to encrypt the save files
            auth_key = login.get_key()

            # start the DBManager
            db_manager = AccountManager(self.path_database, auth_key)
            while True:
                eingabe = input("_> ").split(' ')

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
                        print("pl                   \t Gib alle Accounts in Langform aus.")
                        print("p <ACCOUNT_NAME>     \t Gib die Account Daten aus.")
                        print("get <ACCOUNT_NAME>   \t Fügt das Passwort in den Zwischenspeicher ein.")
                        print("add                  \t Erstelle neuen Account.")
                        print("edit                 \t Editiere einen Account.")
                        print("remove <ACCOUNT_NAME>\t Löschte eine Account.")
                        print("clear                \t Bereinige die Console.")
                        print("save                 \t Änderungen Speichern.")
                        print("exit                 \t Beenden.")
                        print("change pwm           \t Ändere deine Logindaten für den PWM.")
                        print("Das Passwort wird nicht über die Kommandozeile ausgegeben."
                              "Verwende den Befehl 'get <ACCOUNT_NAME> um das Passwort des gesuchten "
                              "Accounts in die Zwischenablage zu speichern.")
                        continue

                elif eingabe[0] == "p":
                    if len(eingabe) == 1:
                        db_manager.print_data(all=True, short=True)
                        continue
                    elif eingabe[1]:
                        db_manager.print_data(name=eingabe[1])
                        continue

                elif eingabe[0] == "pl":
                    if len(eingabe) == 1:
                        db_manager.print_data(all=True, short=False)
                        continue

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

                elif eingabe[0] == "save":
                    if len(eingabe) == 1:
                        db_manager.save()
                        continue

                elif eingabe[0] == "change":
                    if len(eingabe) == 2:
                        if eingabe[1] == "pwm":
                            new_register = Register(self.path_database, self.cypher)
                            new_register.run("ÄNDERUNG DER LOGINDATEN FÜR DEN PWM")
                            new_login = Login(self.path_database, self.cypher)
                            new_login.run("Log dich einmal mit deinen neuen Daten ein.")
                            db_manager.save(path=self.path_database, auth_key=new_login.get_key())
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
                        continue
                print("Eingabe ungültig, schreibe 'help' für Hilfe.")
        else:
            print("Falsches Passwort. Beende Passwort Manager.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some paths.")
    parser.add_argument('--path', type=str, default="", help="Path to save files")
    args = parser.parse_args()
    if os.path.exists(args.path) and os.path.isdir(args.path):
        file_path = args.path
    else:
        file_path = ""

    main = Main(file_path)
    main.run()
