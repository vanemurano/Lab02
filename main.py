import translator as tr

t = tr.Translator()

t.loadDictionary("dictionary.txt")

while(True):

    t.printMenu()

    txtIn = input()
    try:
        if int(txtIn) == 1:
            print("Ok, quale parola devo aggiungere?")
            parole = input()
            t.handleAdd(parole)
        elif int(txtIn) == 2:
            print("Ok, quale parola devo cercare?")
            parola_da_cercare=input()
            t.handleTranslate(parola_da_cercare)
        elif int(txtIn) == 3:
            print("Ok, quale parola devo cercare?")
            parola_wildcard = input()
            t.handleWildCard(parola_wildcard)
        elif int(txtIn) == 4:
            print("Ecco il dizionario completo:")
            t.printTranslator()
        elif int(txtIn) == 5:
            break
        else:
            print("Inserisci un numero compreso tra 1 e 5!")
    except ValueError:
        print("Inserisci un numero compreso tra 1 e 5!")