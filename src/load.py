from crypto import Crypto
from cryptography.fernet import Fernet
import os


class Load:
    @staticmethod
    def load_password(path: str) -> str:
        """
        Load hashed password from file.

        Args:
            path (str): The path to the file
            

        Returns:
            str: The hashed password.
        """

        if os.path.exists(path):
            try:
                # get the first line and return it
                with open(path, 'r') as file:
                    hashed_pw_data = file.readline()
                if hashed_pw_data:
                    return hashed_pw_data
                else:
                    raise SystemExit(f"Keine Daten in der Datei: {path}.")
            except Exception as e:
                print("Fehler!", str(e))
                raise SystemExit(f"Fehler beim lesen der Datei: {path}.")
        else:
            print("Die Datei existiert nicht: %s", path)
            return ""

    @staticmethod
    def load_file(path: str, auth: bytes = b"") -> str:
        """
        Load data from a file.

        Args:
            path (str): The path to the file.
            auth (bytes, optional): Authentication data for decryption. Defaults to b"".

        Returns:
            str: The loaded data.
        """

        if os.path.exists(path):
            try:
                with open(path, 'r') as file:
                    # ignore first line (password data line)
                    file.readline()
                    # read data from second line
                    data_from_file = file.read().strip()

            except Exception as e:
                print("Fehler!", str(e))
                raise SystemExit(f"Fehler beim lesen der Datei: {path}.")

            if data_from_file:
                if auth:
                    return Load._decrypt_data(data_from_file, auth)
                return data_from_file
            else:
                return ""

    @staticmethod
    def _decrypt_data(data: str, auth: bytes) -> str:
        """
        Decrypt data using Fernet encryption.

       Args:
           data (str): The data to be decrypted.
           auth (bytes): The authentication key.

       Returns:
           str: The decrypted data.
       """

        # decrypt data
        try:
            cipher = Fernet(auth)
            return cipher.decrypt(data).decode()
        except Exception as e:
            print("Die Daten konnten nicht entschlüsselt werden, die Datenbank ist defekt.", e)
