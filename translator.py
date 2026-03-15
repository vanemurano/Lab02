from collections import Counter

from dictionary import Dictionary


class Translator:

    default = "La parola cercata non è presente nel dizionario"

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
        if " " not in entry:
            print("Devi inserire la parola e la sua traduzione")
        else:
            if entry.replace(" ", "").isalpha(): #il metodo replace sostituisce gli spazi, per verificare se gli altri caratteri sono tutti lettere
                self.traduttore.addWord(entry.lower())
                print(entry.lower())
                print("Aggiunta!")
            else:
                print("Input non valido: inserisci una parola composta da sole lettere!")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        if query.isalpha():
            if query.lower() in self.traduttore.dizionario.keys():
                stampa=""
                for p in self.traduttore.translate(query):
                    stampa+=f"{p} "
                print(f"{query.lower()} = {stampa}")
            else:
                print(f"{self.default}")
        else:
            print("Input non valido: inserisci una parola composta da sole lettere!")

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        contatore = Counter(query)
        ripetizioni = contatore['?']
        if ripetizioni==1:
            indice=query.find('?')
            parola_strip=query[:indice]+query[indice+1:]
            if parola_strip.isalpha():
                nuovo_diz=self.traduttore.translateWordWildCard(parola_strip, indice)
                if not nuovo_diz: #verifica se il dizionario è vuoto
                    print(self.default)
                else:
                    for (k, v) in nuovo_diz.items():
                        stampa = ""
                        for p in v:
                            stampa += f"{p} "
                        print(f"{k} = {stampa}")
            else:
                print("Inserisci una parola contenente un solo carattere '?' al suo interno")
        else:
            print("Inserisci una parola contenente un carattere '?' al suo interno")

    def printTranslator(self):
        diz_ordinato=dict(sorted(self.traduttore.dizionario.items()))

        for parola, trad in diz_ordinato.items():
            t=""
            for i in range (len(trad)):
                t+=trad[i]+" "
            print(f"{parola} = {t}")