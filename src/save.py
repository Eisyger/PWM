import json
from cryptography.fernet import Fernet
from crypto import Crypto
import os


class Save:

    @staticmethod
    def save_password(path: str, cipher: Crypto, data: list) -> bool:
        """
        Save encrypted password to a file.

        Args:
            path (str): The path to the file.
            cipher (Crypto): The encryption object.
            data (list): The list of strings to be encrypted and hashed, e.g. [username, password].

        Returns:
            bool: True if the password is successfully saved, raises an Error otherwise.
        """
        try:
            if os.path.exists(path):
                # load existing file
                with open(path, 'r') as file:
                    lines = file.readlines()

                # replace the first line with salt in raw form and separated with a colon the new password data
                lines[0] = cipher.salt + ":" + cipher.encrypt_password(data) + "\n"

                # write lines back in file
                with open(path, 'w') as file:
                    file.writelines(lines)
            else:
                # when the file does not exist create new file and save password data
                with open(path, 'w') as file:
                    # use cypher to encrypt the passwort and write it to file
                    file.write(cipher.salt + ":" + cipher.encrypt_password(data) + "\n")

        except Exception as e:
            print("Fehler beim Schreiben der Datei:", path)
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.", str(e))
        return True

    @staticmethod
    def save_file(path: str, account_data: list, auth: bytes = None) -> None:
        """
        Save account data to a file.

        Args:
            path (str): The path to the file.
            account_data (list): The account data to be saved.
            auth (bytes): Authentication data for encryption. Defaults to bytes.
        """

        # create a json from the data
        json_data = json.dumps(account_data, indent=4).encode('utf-8')

        if auth is not None:
            # encrypt parameter json_data as reference
            json_data = Save._encrypt_data(json_data, auth)

        try:
            if os.path.exists(path):
                # first line with the master password data is untouched
                with open(path, 'r') as old_file:
                    pw_data = old_file.readline()
                
                with open(path, 'w') as new_file:
                    new_file.write(pw_data)

                with open(path, 'ab') as file:
                    file.write(json_data)
            else:
                with open(path, 'ab') as file:
                    file.write(json_data)
        except Exception as e:
            print("Fehler beim Schreiben der Datei!", path)
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.",  str(e))

    @staticmethod
    def _encrypt_data(data: bytes, auth: bytes) -> bytes:
        """
        Encrypt data using Fernet encryption.

        Args:
            data (bytes): The data to be encrypted.
            auth (bytes): The authentication key.

        Returns:
            bytes: The encrypted data.
        """

        cipher = Fernet(auth)
        return cipher.encrypt(data)
