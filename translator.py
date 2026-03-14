from dictionary import Dictionary


class Translator:

    def __init__(self):
        self.traduttore=None

    def printMenu(self):
        print("------------------------------\n"
              "   Translator Alien-Italian   \n"
              "------------------------------\n"
              "1. Aggiungi nuova parola\n"
              "2. Cerca una traduzione\n"
              "3. Cerca con wildcard\n"
              "4. Stampa tutto il dizionario\n"
              "5. Exit\n"
              "------------------------------\n")


    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        self.traduttore = Dictionary(dict)

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        self.traduttore.addWord(entry)
        """parola, *traduzioni=entry.strip().split(" ")
        print(f"{parola}, {traduzioni}")"""
        print(entry)
        print("Aggiunta!")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        print (f"{query} = {self.traduttore.translate(query)}")

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass

    def printTranslator(self):
        diz_ordinato=dict(sorted(self.traduttore.dizionario.items()))

        for parola, trad in diz_ordinato.items():
            t=trad
            if isinstance(trad, list):
                t=""
                for i in range (len(trad)):
                    t+=trad[i]+" "
            print(f"{parola} = {t}")