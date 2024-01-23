from crypto import Crypto
from cryptography.fernet import Fernet
import os


class Load:
    @staticmethod
    def load_password(path: str, cipher: Crypto) -> list:
        hashed_data = Load.load_file(path)
        if hashed_data:
            return cipher.decrypt_password(hashed_data)

    @staticmethod
    def load_file(path: str, auth: bytes = b"") -> str:
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
    def _decrypt_data(data: str, auth: bytes):
        # decrypt data
        cipher = Fernet(auth)
        return cipher.decrypt(data).decode()
