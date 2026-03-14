class Dictionary:
    def __init__(self, dict: str):
        self.dizionario= {}
        try:
            with open (dict, "r", encoding="utf-8") as f:
                listaTuple=[]
                for riga in f:
                    parola=riga.split(" ")[0]
                    traduzione=riga.split(" ")[1]
                    listaTuple.append((parola, traduzione))
                    self.dizionario[parola]=traduzione
        except FileNotFoundError:
            print("Nome file non valido")

    def addWord(self, coppia: str):
        coppia_divisa=coppia.strip().split(" ")
        parola=coppia_divisa[0]
        traduzioni=[]
        for i in range(1,len(coppia_divisa)):
            traduzioni.append(coppia_divisa[i])
        if parola in self.dizionario:
            trad_esistenti=self.dizionario.get(parola)
            trad_esistenti.extend(traduzioni)
            self.dizionario[parola]=trad_esistenti
        else:
            self.dizionario[parola]=traduzioni

    def translate(self, parola: str):
        default="La parola cercata non è presente nel dizionario"
        return self.dizionario.get(parola, default)

    def translateWordWildCard(self):
        pass