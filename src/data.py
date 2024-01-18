import json


class Data:
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
        return "\n".join(f"{key.ljust(12)}:\t{value}" for key, value in self.data.items() if key != "PASSWORD") + "\n"

    def get_json(self) -> str:
        return json.dumps(self.data, indent=2)

    @staticmethod
    def account_from_list(string_list: list) -> list:
        account_list = []
        for string_input in string_list:
            try:
                json_data = json.loads(string_input)
                if isinstance(json_data, dict):
                    acc = Data(
                        name_account=json_data.get("ACCOUNT_NAME", ""),
                        login_name=json_data.get("LOGIN_NAME", ""),
                        email=json_data.get("EMAIL", ""),
                        website=json_data.get("WEBSITE", ""),
                        passwort=json_data.get("PASSWORD", "")
                    )
                    account_list.append(acc)
            except json.JSONDecodeError:
                print(f"Fehler beim Decodieren des JSON-Strings: {string_input}")
        return account_list
