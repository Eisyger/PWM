from load import Load
from account import Account


class AccountManager:
    def __init__(self, path: str):
        self.accounts = self.__load_data(path)
        

    def __load_data(self, path):        
        data = Account.account_from_string(Load.load_file(path))
        print(f"{len(data)} Accounts loaded.")
        if data:
            return [Account(d) for d in data]
        
    def print_all():
        for acc in self.accounts:
            print("-----------------------------------------")
            print(acc)
            print("-----------------------------------------")

    def run():
        pass

