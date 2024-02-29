import json
from save import Save
from load import Load
import hashlib
import base64


class AccountData:
    def __init__(self, acc_name: str = "", username: str = "", mail: str = "", website: str = "", password: str = ""):
        self.account_name = acc_name
        self.username = username
        self.mail = mail
        self.website = website
        self.password = password

        self.data_dict = {"ACCOUNT_NAME": self.account_name,
                          "LOGIN_NAME": self.username,
                          "EMAIL": self.mail,
                          "WEBSITE": self.website,
                          "PASSWORD": self.password}

    def __str__(self) -> str:
        return "\n".join(f""
                         f"{key.ljust(12)}:\t{value}"
                         for key, value in self.get_dict().items()
                         if key != "PASSWORD") + "\n"

    def get_dict(self) -> dict:
        return self.data_dict

    @staticmethod
    def creat_acc_from_dict(data: dict):
        return AccountData(data["ACCOUNT_NAME"],
                           data["LOGIN_NAME"],
                           data["EMAIL"],
                           data["WEBSITE"],
                           data["PASSWORD"])

    def keys(self):
        return self.data_dict.keys()
