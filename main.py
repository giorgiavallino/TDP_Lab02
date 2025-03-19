import translator as tr

t = tr.Translator()

t.loadDictionary()

while(True):

    t.printMenu()

    txtIn = input("Inserisci il numero dell'operazione che vuoi svolgere: ")

    if txtIn.isdigit():
        txtIn = int(txtIn)
        if txtIn == 1:
            txtIn = input("Inserisci la parola aliena da aggiungere e la sua relativa traduzione: ")
            txtIn = t.contrInput(txtIn)
            if txtIn != "Il testo non è valido!":
                txtIn = tuple(txtIn.split(" "))
                print(t.handleAdd(txtIn))
            else:
                print(txtIn)
        elif txtIn == 2:
            txtIn = input("Inserisci la parola aliena di cui vuoi cercare la traduzione: ")
            txtIn = t.contrInput(txtIn)
            if txtIn != "Il testo non è valido!":
                print(t.handleTranslate(txtIn))
            else:
                print(txtIn)
        elif txtIn == 3:
            txtIn = input("Inserisci la parola aliena di cui vuoi cercare la traduzione tramite una wildcard: ")
            txtIn = t.contrInputWild(txtIn)
            if txtIn != "Il testo non è valido!":
                parole_possibili = t.generateAllWords(txtIn)
                print(t.handleWildCard(parole_possibili))
            else:
                print(txtIn)
        elif txtIn == 4:
            t.printDict()
        elif txtIn == 5:
            break
        elif txtIn < 1 or txtIn > 5:
            print(f"Il valore inserito non corrisponde a nessuna operazione!")
    else:
        print(f"Il valore inserito non corrisponde a nessuna operazione!")