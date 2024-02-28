import json
from cryptography.fernet import Fernet
from load import Load
from crypto import Crypto


class Save:

    @staticmethod
    def save_password(path: str, cipher: Crypto, data: list) -> bool:
        try:
            # open file, if the file does not exist it gets created
            with open(path, 'w') as file:

                # use cypher to encrypt the passwort and write it to file
                file.write(cipher.encrypt_password(data))

        except Exception as e:
            print("Fehler beim Schreiben der Datei:", path)
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.", str(e))
        return True

    @staticmethod
    def save_file(path: str, account_data: list, auth: bytes = b""):

        # creat a json from the data
        json_data = json.dumps(account_data, indent=4).encode('utf-8')

        if auth:
            # encrypt parameter json_data as reference
            json_data = Save._encrypt_data(json_data, auth)

        try:
            with open(path, 'wb') as file:
                file.write(json_data)
        except Exception as e:
            print("Fehler beim Schreiben der Datei!", path)
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.",  str(e))

    @staticmethod
    def _encrypt_data(data: bytes, auth: bytes):
        # encrypt data
        cipher = Fernet(auth)
        return cipher.encrypt(data)


