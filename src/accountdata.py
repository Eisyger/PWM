class AccountData:
    def __init__(self, acc_name: str = "", username: str = "", mail: str = "", website: str = "", password: str = ""):
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
        return self.data_dict

    def update(self):
        """Update class fields from the dictionary"""
        for key, value in self.data_dict.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @staticmethod
    def create_acc_from_dict(data: dict):
        return AccountData(data["account_name"],
                           data["username"],
                           data["mail"],
                           data["website"],
                           data["password"])

    def keys(self):
        return self.data_dict.keys()
