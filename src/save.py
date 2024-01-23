import json
from cryptography.fernet import Fernet
from load import Load
from crypto import Cryptography


class Save:

    @staticmethod
    def save_password(path: str, cipher: Cryptography, data: list) -> bool:
        try:
            # open file, if the file does not exist it gets created
            with open(path, 'w') as file:

                # use cypher to encrypt the passwort and write it to file
                file.write(cipher.encrypt_and_hash_password(data))

        except Exception as e:
            print("Fehler beim Schreiben der Datei:", path)
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.", str(e))
        return True

    @staticmethod
    def save_file(path: str, account_data: list, auth: bytes):
        # update existing data from file - add new data if possible
        # update parameter account_data as reference
        Save._update_data(path, account_data, auth)

        # creat a json from the data
        json_data = json.dumps(account_data, indent=4).encode('utf-8')

        # encrypt data
        cipher = Fernet(auth)
        encrypted_data = cipher.encrypt(json_data)

        try:
            with open(path, 'wb') as file:
                file.write(encrypted_data)
        except Exception as e:
            print("Fehler beim Schreiben der Datei!", path)
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.",  str(e))

    @staticmethod
    def _update_data(path: str, account_data: list, auth: bytes):
        # load the current date from file, and converts it back to a list via json.loads
        loaded_data = Load.load_file(path, auth)
        if loaded_data:
            current_data = json.loads(loaded_data)

            for data in account_data:
                if data not in current_data:
                    current_data.append(data)
            account_data = current_data
