from data import AccountData
import json


class AccountManager(AccountData):
    def __init__(self, name_account, login_name, email, website, passwort):
        super().__init__(name_account, login_name, email, website, passwort)


# Beispiel-Nutzung:
manager = AccountManager(
    name_account="Beispiel-Account",
    login_name="beispiel_user",
    email="beispiel@example.com",
    website="https://www.beispiel.com",
    passwort="geheimesPasswort"
)

# JSON-String der Daten ausgeben
json_daten = manager.get_json()
print(json_daten)
print(manager)
