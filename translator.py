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
        return print(stringa)

    def loadDictionary(self):
        self.dizionario.readDict()
        return self.dizionario

    def handleAdd(self, entry): # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parola_aliena = entry[0]
        if len(entry) == 2:
            if parola_aliena in self.dizionario.dizionario.keys():
                traduzioni = []
                parola_umana = self.dizionario.dizionario[parola_aliena]
                if isinstance(parola_umana, list):
                    for parola in parola_umana:
                        traduzioni.append(parola)
                else:
                    traduzioni.append(parola_umana)
                del self.dizionario.dizionario[parola_aliena]
                traduzioni.append(entry[1])
                self.dizionario.addWord(parola_aliena, traduzioni)
            else:
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
            stringa = f"La traduzione della parola aliena {query} non è ancora disponibile."
        return stringa

    def generateAllWords(self, parola):
        parole = []
        for lettera in "abcdefghijklmnopqrstuvwxyz":
            parola_da_aggiungere = parola.replace("?", lettera, 1)
            parola_da_aggiungere = parola_da_aggiungere.lower()
            parole.append(parola_da_aggiungere)
        return parole

    def handleWildCard(self, parole_possibili): # query is a string with a ? --> <par?la_aliena>
        for parola_possibile in parole_possibili:
            for chiave in self.dizionario.dizionario.keys():
                if parola_possibile == chiave:
                    return self.handleTranslate(parola_possibile) # la chiamata deve essere fatta direttamente
                    # sull'oggetto Translator perché è quest'ultimo l'unico a possedere la funzione handleTranslate !

    def contrInput(self, txt):
        testo_senza_spazi = txt.replace(" ", "")
        if testo_senza_spazi.isalpha() == False:
            txt = f"Il testo non è valido!"
        else:
            txt = txt.lower()
        return txt

    def contrInputWild(self, txt):
        testo_senza_spazi = txt.replace(" ", "")
        if any(char.isdigit() for char in testo_senza_spazi) == True:
            txt = f"Il testo non è valido"
        else:
            txt = txt
        return txt

    def printDict(self):
        for chiave in self.dizionario.dizionario.keys():
            traduzione = self.dizionario.dizionario[chiave]
            stringa = f"{chiave}: {traduzione}"
            print(stringa)