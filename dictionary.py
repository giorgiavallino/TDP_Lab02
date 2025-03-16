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
                parola_minuscola = parola
                parole.append(parola_minuscola)
            for parola in parole:
                chiave = parola[0].lower()
                valore = parola[1].lower()
                self.dizionario[chiave] = valore
            return self.dizionario

    def addWord(self, parola_aliena, parola_umana):
        self.dizionario[parola_aliena] = parola_umana
        return self.dizionario

    def translate(self, parola_aliena):
        return self.dizionario[parola_aliena]

    def translateWordWildCard(self):
        pass