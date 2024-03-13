import string


class Restrictions:

    @staticmethod
    def check_username(username: str) -> bool:
        """
        Check the validity of the username.

        Args:
            username (str): The username to be checked.

        Returns:
            bool: True if the username meets the criteria, False otherwise.
        """

        # Check the username
        if 3 < len(username) < 16 and username.isalnum():
            return True
        else:
            print("#" * 50)
            print("Fehler:")
            print("Der Username muss länger als 3 Zeichen sein.")
            print("Nur Zahlen und Buchstaben werden akzeptiert.")
            print("#" * 50)

            return False

    @staticmethod
    def check_password(password: str) -> bool:
        if (12 < len(password) < 1337
                and any(c.isupper() for c in password)
                and any(c.islower() for c in password)
                and any(c.isdigit() for c in password)
                and any(c.isalnum() for c in password)
                and any(c in string.punctuation for c in password)):
            return True
        else:
            print("#" * 50)
            print("Fehler", "Das Passwort muss mindestens 12 Zeichen lang sein.")
            print("Es muss mindestens einen Großbuchstaben, einen Kleinbuchstaben,")
            print("eine Zahl und ein Sonderzeichen enthalten.")
            print("#" * 50)

            return False
