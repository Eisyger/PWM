from cryptography import Cryptography
from load import Load
from pwinput import PWInput
import getpass

class Login(PWInput):
    def __init__(self, path: str, cypher: Cryptography):
        super().__init__()
        self.path = path
        self.cypher = cypher        

    def run(self):
        super().run("LOGIN")
        data = [self.username, self.password]
        hashed_data = self.cypher.encrypt(data)
        hashed_pw = Load.load_file(path)
        if Cryptography.check_hash(hashed_data, hashed_pw):
            return True
        else:
            return False       
