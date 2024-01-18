from data import AccountData
import json

class AccountManager(AccountData):
    def __init__(self, nameAccount, loginName, loginEmail, website, passwort):
        super().__init__()  
        self.nameAccount = nameAccount
        self.loginName = loginName
        self.loginEmail = loginEmail
        self.website = website
        self.passwort = passwort
        self.daten_dict = self._generate_dict()

    def _generate_dict(self):
        return {
            "nameAccount": self.nameAccount,
            "loginName": self.loginName,
            "loginEmail": self.loginEmail,
            "website": self.website,
            "passwort": self.passwort,
        }

    def write(self) -> str:
        return json.dumps(self.daten_dict, indent=2)

# Beispiel-Nutzung:
manager = AccountManager(
    nameAccount="Beispiel-Account",
    loginName="beispiel_user",
    loginEmail="beispiel@example.com",
    website="https://www.beispiel.com",
    passwort="geheimesPasswort"
)

# JSON-String der Daten ausgeben
json_daten = manager.write()
print(json_daten)
