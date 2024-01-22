from cryptography import Cryptography


class Load:
    @staticmethod
    def decrypt_and_load(path: str, cipher: Cryptography) -> list:
        hashed_data = Load.load_file(path)
        return cipher.decrypt(hashed_data)
    
    @staticmethod
    def load_file(path: str) -> str:
        # Loading data from file and return as a string
        try:
            with open(path, 'r') as file:
                data = file.read().strip()
        except Exception as e:
            print("Fehler!", str(e))
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.")
        return data
