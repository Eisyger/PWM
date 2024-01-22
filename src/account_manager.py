from load import Load
from src.account import Account


class AccountManager:
    def __init__(self, path: str):
        self.accounts = []
        data_from_file: str = Load.load_file(path)
        data = Account.account_from_string(data_from_file)

        for d in data:
            self.accounts.append(Account(d))

        for acc in self.accounts:
            print(acc)

"""TODO json dateien müssen als liste mit eckigen klammern gespeichert werden. 
sonst können nur einzelne daten gelesen werden."""
a = AccountManager("../src/save_file_data.mpw")
