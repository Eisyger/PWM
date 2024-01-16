from register import Register
from cryptography import Cryptography
import os


class Main:
    def __init__(self):
        self.path = "save_file.mpw"
        self.salt = "1|<y18#+-.fvtvk.49610/*"
        self.pepper = "anti_rainbow"
        self.cypher = Cryptography(self.salt, self.pepper)

    def run(self):
        if os.path.exists(self.path):
            pass  # Implement Login
        else:
            register = Register(self.path, self.cypher)
            register.run()


if __name__ == "__main__":
    main = Main()
    main.run()
