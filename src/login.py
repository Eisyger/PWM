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
        # implementiere hier den vergleich der eingabe und dem in der datai gespeicherten hash

