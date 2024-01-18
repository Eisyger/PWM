import json


class AccountData:
    def __init__(self,
                 name_account: str = "",
                 login_name: str = "",
                 email: str = "",
                 website: str = "",
                 passwort: str = ""):
        self.data = {
            "ACCOUNT_NAME": name_account,
            "LOGIN_NAME": login_name,
            "EMAIL": email,
            "WEBSITE": website,
            "PASSWORD": passwort,
        }

    def __str__(self) -> str:
        return "\n".join(f"{key.ljust(12)}:\t{value}" for key, value in self.data.items() if key != "PASSWORD")

    def get_json(self) -> str:
        return json.dumps(self.data, indent=2)
