import json
from save import Save

class Data:
    def __init__(self,
                 name_account: str = "",
                 login_name: str = "",
                 email: str = "",
                 website: str = "",
                 password: str = ""):
        self.data = {
            "ACCOUNT_NAME": name_account,
            "LOGIN_NAME": login_name,
            "EMAIL": email,
            "WEBSITE": website,
            "PASSWORD": password,
        }

    def __str__(self) -> str:
        return "\n".join(f"{key.ljust(12)}:\t{value}" for key, value in self.data.items() if key != "PASSWORD") + "\n"

    def get_json(self) -> str:
        return json.dumps(self.data, indent=2)



#data1 = Data("Facebook", "Marie", "asdf@gmx.de", "facebook.de", "123")
#data2 = Data("Google", "Marie", "asdf@gmx.de", "google.de", "1234")

#Save.save_json("save_file_data.mpw", [data1.get_json(), data2.get_json()])
