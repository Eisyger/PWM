from load import Load
from account import Account


class AccountManager:
    def __init__(self, path: str):
        self.accounts = self.__load_data(path)
        

    def __load_data(self, path):        
        data = Account.account_from_string(Load.load_file(path))
        if data:
            return [Account(d) for d in data]
 

"""TODO json dateien müssen als liste mit eckigen klammern gespeichert werden. 
sonst können nur einzelne daten gelesen werden."""
a = AccountManager("save_file_data.mpw")
