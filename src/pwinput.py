import getpass

class PWInput:
    def __init__(self):        
        self.username = ""
        self.password = ""

    def run(self, startText: str):
        print(startText)
        try:
            while True:
                self.username = input("Eingabe Username: ")
                self.password = getpass.getpass(prompt="Eingabe Passwort: ") 
        except Exception as e:
            print(e)
            raise SystemExit("Programm wird beendet.")