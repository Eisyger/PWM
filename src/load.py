from crypto import Crypto
from cryptography.fernet import Fernet
import os


class Load:
    @staticmethod
    def load_password(path: str, cipher: Crypto) -> list:
        """
        Load password from file and decrypt it.

        Args:
            path (str): The path to the file.
            cipher (Crypto): The encryption object.

        Returns:
            list: The decrypted password.
        """

        hashed_data = Load.load_file(path)
        if hashed_data:
            return cipher.decrypt_password(hashed_data)

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
