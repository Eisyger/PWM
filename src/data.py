class AccountData:
    def __init__(self):
        self.nameAccount = ""
        self.loginName = ""
        self.LoginEmail = ""
        self.website = ""
        self.password = ""
        self.note = ""

    def __str__(self) -> str:
        return (
            f"Account Name   : {self.nameAccount}\n"
            f"Website        : {self.website}\n"
            f"Login Name     : {self.loginName}\n"
            f"Login Email    : {self.LoginEmail}\n"            
            f"Notizen        : {self.note}"
        )