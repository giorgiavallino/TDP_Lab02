from dictionary import Dictionary

class Translator:

    def __init__(self, dizionario = Dictionary()):
        self.dizionario = dizionario

    def __repr__(self):
        return self.dizionario

    def __str__(self):
        return self.dizionario

    def printMenu(self):
        stringa = ("TRANSLATOR ALIEN-ITALIAN\n"
                   "1. Aggiungi una nuova parola\n"
                   "2. Cerca una traduzione\n"
                   "3. Cerca con una wildcard\n"
                   "4. Stampa tutto il dizionario\n"
                   "5. Exit")
        return stringa

    def loadDictionary(self):
        self.dizionario = self.dizionario.readDict()
        return self.dizionario

    def handleAdd(self, entry): # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query): # query is a string <parola_aliena>
        pass


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass

t = Translator()
print(t.printMenu())
print(t.loadDictionary())
print(t.handleTranslate())