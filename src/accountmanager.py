from data import AccountData
import json

class AccountManager(AccountData):
    def __init__(self, nameAccount, loginName, loginEmail, website, passwort):
        super().__init__(nameAccount, loginName, loginEmail, website, passwort)  
        

    

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
