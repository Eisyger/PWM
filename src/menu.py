class Menu:
    def __init__(self, ):
        self.options = {"ADD": self.__add,
                        "EDIT": self.__edit,
                        "GET": self.__get,
                        "DELETE": self.__delete,
                        "PRINT": self.__print_all,
                        "PRINTALL": self.__print_all}

    def __print_all(self) -> str:
        # Logik für die "PRINT" und "PRINTALL"-Funktion
        return "PRINT-Methode aufgerufen"

    def __add(self) -> str:
        # Logik für die "ADD"-Funktion
        return "ADD-Methode aufgerufen"

    def __edit(self) -> str:
        # Logik für die "EDIT"-Funktion
        return "EDIT-Methode aufgerufen"

    def __get(self) -> str:
        # Logik für die "GET"-Funktion
        return "GET-Methode aufgerufen"

    def __delete(self) -> str:
        # Logik für die "DELETE"-Funktion
        return "DELETE-Methode aufgerufen"

    def __help(self):
        for key in self.options.keys():
            print(key)

    def menu(self) -> str:
        pass