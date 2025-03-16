import translator as tr

t = tr.Translator()

while(True):

    t.printMenu()

    t.loadDictionary()

    txtIn = input("Inserisci il numero dell'operazione che vuoi svolegere: ")

    if int(txtIn) == 1:
        txtIn = input("Inserisci la parola aliena da aggiungere e la sua relativa traduzione: ")
        txtIn = t.contrInput(txtIn)
        if txtIn != "Il testo non è valido!":
            print(t.handleAdd(txtIn))
        else:
            print(txtIn)
    elif int(txtIn) == 2:
        pass
    elif int(txtIn) == 3:
        pass
    elif int(txtIn) == 4:
        break
    else:
        print(f"Il valore inserito non corrisponde a nessuna operazione!")