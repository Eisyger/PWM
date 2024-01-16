from cryptography import Cryptography


class Save:

    @staticmethod
    def encrypt_and_save_file(path: str, cipher: Cryptography, data: list) -> bool:
        try:
            with open(path, 'w') as file:
                file.write(cipher.encrypt(data))
                print("Speichern?")
        except Exception as e:
            print("Fehler!", str(e))
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.")

        return True
