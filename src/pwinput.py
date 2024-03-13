import getpass
from restrictions import Restrictions


class PWInput:
    def __init__(self):
        self.username = ""
        self.password = ""

    def run(self, start_text=None) -> bool:
        """
        Create a query of the username and password in the console.
        Specifications regarding the inputs are governed by the restrictions.py.
        Return True if the input was valid, and False if not.

        Args:
            start_text (str, optional): The text to display at the beginning of the query. Defaults to None.

        Returns:
            bool: True if the input was valid, and False if not.
        """

        if start_text is not None:
            print(start_text)

        if self._user_input():
            if self._password_input():
                return True
            return False
        return False

    def _user_input(self) -> bool:
        user = input("Eingabe Username: ")
        if Restrictions.check_username(user):
            self.username = user
            return True
        return False

    def _password_input(self) -> bool:
        pw = getpass.getpass(prompt="Eingabe Passwort: ")
        if Restrictions.check_password(pw):
            self.password = pw
            return True
        return False
