import hmac
import hashlib


class Cryptography:
    def __init__(self, salt: str, pepper: str):
        self.salt = salt
        self.pepper = pepper

    def encrypt(self, data: list) -> str:
        if not data:
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.")

        try:
            data = " ".join(data)
        except TypeError:
            print("Der Parameter data der Methode enrcypt muss eine Liste aus strings sein.")
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.")

        # Data to Hash
        hash_data = data.encode('utf-8') + self.salt.encode('utf-8')

        # HMAC-Hashing
        hashed_data = hmac.new(self.pepper.encode('utf-8'), hash_data, hashlib.sha256).hexdigest()

        return hashed_data
