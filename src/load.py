from src.crypto import Cryptography
from cryptography.fernet import Fernet


class Load:
    @staticmethod
    def decrypt_and_load(path: str, cipher: Cryptography) -> list:
        hashed_data = Load.load_file(path)
        return cipher.decrypt(hashed_data)
    
    @staticmethod
    def load_file(path: str, auth: bytes = b"") -> str:

        if auth:
            # Load data from file
            try:
                with open(path, 'rb') as file:
                    data_from_file = file.read().strip()
            except Exception as e:
                print("Fehler!", str(e))
                raise SystemExit("Programm wird beendet aufgrund eines Fehlers.")

            if data_from_file:
                try:
                    # decrypt data
                    cipher = Fernet(auth)
                    decrypted_data = cipher.decrypt(data_from_file)

                except Exception as e:
                    print("Fehler!", str(e))
                    raise SystemExit("Programm wird beendet aufgrund eines Fehlers.")

                return decrypted_data.decode()
            else:
                return ""

        else:
            # Loading data from file and return as a string
            try:
                with open(path, 'r') as file:
                    data_from_file = file.read().strip()
            except Exception as e:
                print("Fehler!", str(e))
                raise SystemExit("Programm wird beendet aufgrund eines Fehlers.")
            return data_from_file
