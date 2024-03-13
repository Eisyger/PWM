class AccountData:
    def __init__(self, acc_name: str = "", username: str = "", mail: str = "", website: str = "", password: str = ""):
        """
        Initialize AccountData instance.

        Args:
            acc_name (str, optional): Account name. Defaults to "".
            username (str, optional): Username. Defaults to "".
            mail (str, optional): Email. Defaults to "".
            website (str, optional): Website. Defaults to "".
            password (str, optional): Password. Defaults to "".
        """

        self.account_name = acc_name
        self.username = username
        self.mail = mail
        self.website = website
        self.password = password

        self.data_dict = {"account_name": self.account_name,
                          "username": self.username,
                          "mail": self.mail,
                          "website": self.website,
                          "password": self.password}

    def __str__(self) -> str:
        return "\n".join(f""
                         f"{key.ljust(12)}:\t{value}"
                         for key, value in self.get_dict().items()
                         if key != "password") + "\n"

    def get_dict(self) -> dict:
        """Return data dictionary."""
        return self.data_dict

    def update(self):
        """Update class fields from the dictionary."""
        for key, value in self.data_dict.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @staticmethod
    def create_acc_from_dict(data: dict):
        """Create an AccountData instance from a dictionary."""
        return AccountData(data["account_name"],
                           data["username"],
                           data["mail"],
                           data["website"],
                           data["password"])

    def keys(self):
        """Return keys of the data dictionary."""
        return self.data_dict.keys()
