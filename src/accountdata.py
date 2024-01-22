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
                         for key, value in self._get_dict().items()
                         if key != "PASSWORD") + "\n"

    def _get_dict(self) -> dict:
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

    def save(self, path: str, auth_key: bytes):
        Save.save_file(path, [self._get_dict()], auth_key)


"""
d1 = AccountData("Facebook", "Marie", "asdf@gmx.de", "facebook.de", "123")
d2 = AccountData("Google", "Marie", "asdf@gmx.de111111", "google.de", "1234")


seed = "DeinEigenerFaktor"

# Erzeuge einen Schlüssel durch Hashing der Seed-Zeichenkette
key_bytes = hashlib.sha256(seed.encode('utf-8')).digest()

# Konvertiere den Schlüssel in base64
base64_key = base64.urlsafe_b64encode(key_bytes)

d1.save("save_file_data.mpw", base64_key)
print(json.loads(Load.load_file("save_file_data.mpw", base64_key)))"""

