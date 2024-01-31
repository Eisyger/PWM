import json
import os
from load import Load
from accountdata import AccountData


class AccountManager:
    def __init__(self, path_data: str, auth_key: bytes):
        self.accounts = []
        self.auth_key = auth_key
        self.path_data = path_data

        # load data from file and generate list
        if os.path.exists(path_data):
            self.accounts = self.__load_data_from_file()
            print("Daten geladen.")
        else:
            print("Keine Daten gefunden.")

    def __load_data_from_file(self):
        data_from_file = Load.load_file(self.path_data, self.auth_key)
        if data_from_file:
            json_from_file = json.loads(data_from_file)
            return [AccountData.creat_acc_from_dict(account) for account in json_from_file]

    def __print_all(self, short=True):
        index = 1
        print("Auflistung aller Accounts:")
        for acc in self.accounts:
            print("-" * 50)
            if short:
                print(acc.account_name)
            else:
                print(acc)
            index += 1
        print("-" * 50)
        print(f"Es wurden die Daten von {index} Accounts ausgegeben.")

    def create_test_data(self):
        print("Nock keine Accounts vorhanden. Willst du einen neuen Account anlegen?")
        print("Anlegen von Accounts.")
        d1 = AccountData("Facebook", "Marie", "asdf@gmx.de", "facebook.de", "123")
        d2 = AccountData("Instagram", "Marie", "asdf@gmx.de", "instagram.de", "123")
        d3 = AccountData("gdasf", "Marie", "asdf@gmx.de", "instagram.de", "123")
        d4 = AccountData("asdf", "Marie", "asdf@gmx.de", "instagram.de", "123")
        print("Speichere Accounts.")
        d1.save(self.path_data, self.auth_key)
        d2.save(self.path_data, self.auth_key)
        d3.save(self.path_data, self.auth_key)
        d4.save(self.path_data, self.auth_key)

        print("Lade Accounts.")
        self.accounts = self.__load_data_from_file()
        print("Geladen!")

        for acc in self.accounts:
            print(str(acc))

        """TODO encryption mit parameter schalten, um speicherinhalt zu prüfen."""

    def menu(self) -> str:
        pass

