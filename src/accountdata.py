import json
from save import Save
from load import Load
import hashlib
import base64


class AccountData:
    def __init__(self,
                 account_name: str = "",
                 login_name: str = "",
                 email: str = "",
                 website: str = "",
                 password: str = ""):

        self.account_name = account_name
        self.login_name = login_name
        self.email = email
        self.website = website
        self.password = password

    def __str__(self) -> str:
        return "\n".join(f""
                         f"{key.ljust(12)}:\t{value}"
                         for key, value in self.get_dict().items()
                         if key != "PASSWORD") + "\n"

    def get_dict(self) -> dict:
        return {
            "ACCOUNT_NAME": self.account_name,
            "LOGIN_NAME": self.login_name,
            "EMAIL": self.email,
            "WEBSITE": self.website,
            "PASSWORD": self.password,
        }

    @staticmethod
    def creat_acc_from_dict(data: dict):
        return AccountData(data["ACCOUNT_NAME"],
                           data["LOGIN_NAME"],
                           data["EMAIL"],
                           data["WEBSITE"],
                           data["PASSWORD"])




