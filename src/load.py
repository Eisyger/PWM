from cryptography import Cryptography
import hmac

class Load:
    @staticmethod
    def load_and_decrypt_file(path: str, cipher: Cryptography) -> list:
        # Loading masterpassword hash
        try:
            with open(path, 'r') as file:
                hashed_data = file.read().strip()
        except Exception as e:
            print("Fehler!", str(e))
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.")

        return cipher.decrypt(hashed_data)

