import json
import os
import clipboard
from load import Load
from save import Save
from accountdata import AccountData


class AccountManager:
    def __init__(self, path_data: str, auth_key: bytes):
        self._accounts = []
        self._auth_key = auth_key
        self._path_data = path_data

        # load data from file and generate list
        if os.path.exists(path_data):
            self._accounts = self.__load_data_from_file()
            print("Daten geladen.")
        else:
            print("#" * 50)
            print("Keine Daten gefunden.")
            print("#" * 50)

    def __load_data_from_file(self):
        data_from_file = Load.load_file(self._path_data, self._auth_key)
        if data_from_file:
            json_from_file = json.loads(data_from_file)
            return [AccountData.creat_acc_from_dict(account) for account in json_from_file]

    def print_data(self, name="", all=False, short=True, ):
        i = 0
        print("Auflistung aller Accounts:")
        print("-" * 50)

        for acc in self._accounts:
            i += 1

            if acc.account_name == name and not all:
                print(f"{i}:\n{acc}")

            if all:
                if short:
                    print(f"{i}: {acc.account_name}")
                else:
                    print(f"{i}:\n{acc}")

        print("-" * 50)

    def get_password(self, name):
        for acc in self._accounts:
            if acc.account_name == name:
                clipboard.copy_to_clipboard(acc.password)
                print("Passwort in Zwischenablage gespeichert.")

    def remove(self, name):
        for i, acc in enumerate(self._accounts):
            if acc.account_name == name:
                self._accounts.pop(i)
                print(f"Der Account {name} wurde gelöscht.")

    def save(self):
        Save.save_file(self._path_data, [acc.get_dict() for acc in self._accounts], self._auth_key)

    # TODO Add und Edit methode hinzufügen

    def create_test_data(self):
        """Generiert eine Testdatenbank. Führe dazu test_account_manager.py aus!"""

        print("Noch keine Accounts vorhanden. Willst du einen neuen Account anlegen?")
        print("Anlegen von Accounts.")
        d1 = AccountData("Facebook", "Marie", "asdf@gmx.de", "facebook.de", "sarhaee")
        d2 = AccountData("Instagram", "Marie", "asdf@gmx.de", "instagram.de", "128791aer49g3")
        d3 = AccountData("gdasf", "Marie", "asdf@gmx.de", "instagram.de", "c1e501123gv ")
        d4 = AccountData("asdf", "Marie", "asdf@gmx.de", "instagram.de", "sdsadg79)8/")
        print("Speichere Accounts.")
        accounts = [d1, d2, d3, d4]
        Save.save_file(self._path_data, [acc.get_dict() for acc in accounts], self._auth_key)

        print("Lade Accounts.")
        self._accounts = self.__load_data_from_file()
        print("Geladen!")

        for acc in self._accounts:
            print(str(acc))
