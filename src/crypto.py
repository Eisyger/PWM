import hmac
import hashlib


class Cryptography:
    def __init__(self, salt: str, pepper: str):
        self.salt = salt
        self.pepper = pepper

    def encrypt_and_hash_password(self, data: list, seperator=" ") -> str:
        if not data:
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.")

        try:
            # concat data
            data = seperator.join(data)
        except TypeError:
            print("Der Parameter data der Methode encrypt_and_hash_password muss eine Liste aus strings sein.")
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.")

        # add salt to data
        encoded_data = data.encode('utf-8') + self.salt.encode('utf-8')

        # HMAC-Hashing
        hashed_data = hmac.new(self.pepper.encode('utf-8'), encoded_data, hashlib.sha256).hexdigest()

        return hashed_data

    def decrypt(self, hashed_data: str) -> list:
        """TODO decrypt funktioniert noch nicht"""
        try:
            # Reverse HMAC-Hashing
            hash_data = bytes.fromhex(hashed_data)
            original_data = hmac.new(self.pepper.encode('utf-8'), hash_data[:-len(self.salt.encode('utf-8'))],
                                     hashlib.sha256).digest()
            original_data = original_data.decode('utf-8')

            # Split the original data into a list of strings
            decrypted_data = original_data.split(" ")

            return decrypted_data
        except Exception as e:
            print(f"Fehler bei der Entschlüsselung: {str(e)}")
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.")
