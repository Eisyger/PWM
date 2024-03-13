import hmac
import hashlib
import base64


class Crypto:
    def __init__(self, salt: str, pepper: str):
        self.salt = salt
        self.pepper = pepper

    def encrypt_password(self, data: list, separator: str = " ") -> str:
        """
        Encrypt and hash the password data.

        Args:
            data (list): The list of strings to be encrypted and hashed.
            separator (str, optional): The separator used to join the data strings. Defaults to " ".

        Returns:
            str: The hashed password.
        """

        if not data:
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.")

        try:
            # concat data
            data = separator.join(data)
        except TypeError:
            print("Der Parameter data der Methode encrypt_and_hash_password muss eine Liste aus strings sein.")
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.")

        # add salt to data
        encoded_data = data.encode('utf-8') + self.salt.encode('utf-8')

        # HMAC-Hashing
        hashed_data = hmac.new(self.pepper.encode('utf-8'), encoded_data, hashlib.sha256).hexdigest()

        return hashed_data

    def decrypt_password(self, hashed_data: str, separator: str = " ") -> list:
        """
        Decrypt the hashed password data.

        Args:
            hashed_data (str): The hashed password to decrypt.
            separator (str, optional): The separator used to split the decrypted data into a list. Defaults to " ".

        Returns:
            list: The decrypted password data as a list of strings.
        """

        try:
            # Reverse HMAC-Hashing
            hash_data = bytes.fromhex(hashed_data)
            original_data = hmac.new(self.pepper.encode('utf-8'),
                                     hash_data[:-len(self.salt.encode('utf-8'))],
                                     hashlib.sha256).digest()

            original_data = original_data.decode('utf-8')

            # Split the original data into a list of strings
            decrypted_data = original_data.split(separator)

            return decrypted_data

        except Exception as e:
            print(f"Fehler bei der Entschlüsselung: {str(e)}")
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.")

    @staticmethod
    def generate_fenet_key(seed: str) -> bytes:
        """
        Generate a Fernet key from a seed.

        Args:
            seed (str): The seed string.

        Returns:
            bytes: The Fernet key.
        """

        key_bytes = hashlib.sha256(seed.encode('utf-8')).digest()
        base64_key = base64.urlsafe_b64encode(key_bytes)
        return base64_key

