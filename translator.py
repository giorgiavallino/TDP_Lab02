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
        self.dizionario.readDict()
        return self.dizionario

    def handleAdd(self, entry): # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parola_aliena = entry[0]
        if len(entry) == 2:
            self.dizionario.addWord(parola_aliena, entry[1])
        else:
            traduzioni = []
            for i in range(1, len(entry)):
                traduzioni.append(entry[i])
            self.dizionario.addWord(parola_aliena, traduzioni)
        return self.dizionario

    def handleTranslate(self, query):# query is a string <parola_aliena>
        if query in self.dizionario.dizionario.keys():
            traduzione = self.dizionario.translate(query)
            if isinstance(traduzione, list):
                traduzione = ", ".join(traduzione)
                stringa = f"Le traduzioni della parola aliena {query} sono: {traduzione}."
            else:
                stringa = f"La traduzione della parola aliena {query} è: {traduzione}."
        else:
            stringa = f"La tarduzione della parola aliena {query} non è ancora disponibile."
        return stringa

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass

t = Translator()
print(t.printMenu())
print(t.loadDictionary())
print(t.handleTranslate("kadnajkbdabkan"))
tupla = ("kim", "kardashian", "jenner")
print(t.handleAdd(tupla))
print(t.handleTranslate("kim"))