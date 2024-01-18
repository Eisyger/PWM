class AccountData:
    def __init__(self, nameAccount, loginName, loginEmail, website, passwort):
        self.data = {
            "nameAccount": nameAccount,
            "loginName": loginName,
            "loginEmail": loginEmail,
            "website": website,
            "passwort": passwort,
        }

    def __str__(self) -> str:
        return "".join(f"{key}      :       {value}" for key, value in self.data.items())
    
    def _generate_dict(self):
        return {
            "nameAccount": self.nameAccount,
            "loginName": self.loginName,
            "loginEmail": self.loginEmail,
            "website": self.website,
            "passwort": self.passwort,
        }

    def write_json(self) -> str:
        return json.dumps(self.daten_dict, indent=2)