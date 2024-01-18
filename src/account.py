from data import Data
import json


class Account(Data):
    def __init__(self, name_account, login_name, email, website, passwort):
        super().__init__(name_account, login_name, email, website, passwort)
