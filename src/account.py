from data import Data
import json


class Account(Data):
    def __init__(self, data: Data):
        super().__init__(data.data["ACCOUNT_NAME"], data.data["LOGIN_NAME"], data.data["EMAIL"],
                         data.data["WEBSITE"], data.data["PASSWORD"])

    @staticmethod
    def account_from_string(string_from_file: str) -> list:
        account_list = []

        print("Start")
        for string in string_from_file.strip().split('#'):
            try:
                json_data = json.loads(string)
                if isinstance(json_data, dict):
                    acc = Data(
                        name_account=json_data.get("ACCOUNT_NAME", ""),
                        login_name=json_data.get("LOGIN_NAME", ""),
                        email=json_data.get("EMAIL", ""),
                        website=json_data.get("WEBSITE", ""),
                        password=json_data.get("PASSWORD", "")
                    )
                    account_list.append(acc)
            except json.JSONDecodeError:
                print(f"Fehler beim Decodieren des JSON-Strings: {string}")
        return account_list
