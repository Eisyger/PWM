import json

from load import Load
from src.account import Account


class AccountManager:
    def __init__(self, path: str, auth_key: bytes):
        # load data from file and generate list
        data_from_file = Load.load_file(path, auth_key)
        self.accounts = json.loads(data_from_file)

        print(self.accounts)


