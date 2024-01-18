from cryptography import Cryptography


class Save:

    @staticmethod
    def encrypt_and_save(path: str, cipher: Cryptography, data: list) -> bool:
        try:
            with open(path, 'w') as file:
                file.write(cipher.encrypt_and_hash(data))
        except Exception as e:
            print("Fehler beim Schreiben der Datei!", str(e))
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.")
        return True

    @staticmethod
    def save_json(path: str, json_data: list):
        try:
            with open(path, 'a') as file:
                for d in json_data:
                    file.write("\n" + str(d) + "#")
        except Exception as e:
            print("Fehler beim Schreiben der Datei!", str(e))
            raise SystemExit("Programm wird beendet aufgrund eines Fehlers.")

