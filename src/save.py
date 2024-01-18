from cryptography import Cryptography


class Save:

    @staticmethod
    def encrypt_and_save(path: str, cipher: Cryptography, data: list) -> bool:
        try:
            with open(path, 'w') as file:
                file.write(cipher.encrypt_and_hash(data))
        except Exception as e:
            print("Fehler!", str(e))
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.")
        return True
