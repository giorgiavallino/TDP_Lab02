class Dictionary:

    def __init__(self, dizionario = {}):
        self.dizionario = dizionario

    def __repr__(self):
        return f"{self.dizionario}"

    def __str__(self):
        return f"{self.dizionario}"

    def readDict(self):
        with open("dictionary.txt", "r") as file:
            parole = []
            for linea in file:
                parola = linea.split()
                parole.append(parola)
            for parola in parole:
                self.dizionario[parola[0]] = parola[1]
            return self.dizionario

    def addWord(self):
        pass

    def translate(self, parola_aliena):
        pass

    def translateWordWildCard(self):
        pass