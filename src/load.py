from crypto import Cryptography
from cryptography.fernet import Fernet
import os


class Load:
    @staticmethod
    def decrypt_and_load(path: str, cipher: Cryptography) -> list:
        hashed_data = Load.load_file(path)
        if hashed_data:
            return cipher.decrypt(hashed_data)
    
    @staticmethod
    def load_file(path: str, auth: bytes = b"") -> str:
        if os.path.exists(path):
            if auth:
                return Load._encrypted_load(path, auth)
            else:
                return Load._normal_load(path)

    @staticmethod
    def _normal_load(path: str):
        # load data from file
        try:
            with open(path, 'r') as file:
                data_from_file = file.read().strip()
        except Exception as e:
            print("Fehler!", str(e))
            raise SystemExit(f"Fehler beim lesen der Datei: {path}.")
        if data_from_file:
            return data_from_file
        else:
            return ""

    @staticmethod
    def _encrypted_load(path: str, auth: bytes):
        # load data from encrypted file, with the auth_key
        try:
            with open(path, 'rb') as file:
                data_from_file = file.read().strip()

        except Exception as e:
            print("Fehler!", str(e))
            raise SystemExit(f"Fehler beim lesen der Datei: {path}.")

        if data_from_file:
            try:
                # decrypt data
                cipher = Fernet(auth)
                decrypted_data = cipher.decrypt(data_from_file)

            except Exception as e:
                print("Fehler!", str(e))
                raise SystemExit(f"Fehler decodierten der Datei: {path}")

            return decrypted_data.decode()
        else:
            return ""

