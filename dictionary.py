from collections import Counter


class Dictionary:

    def __init__(self, dict: str): #dict è il nome del file di testo
        self.dizionario= {}
        self.nome_file=dict
        try:
            with open (dict, "r", encoding="utf-8") as f:
                for riga in f:
                    parole=riga.split()
                    if len(parole)==0:
                        continue #ignora le righe vuote e passa alla riga successiva
                    else:
                        parola=parole[0]
                        if len(parole)==2:
                            traduzione=[parole[1]]
                        else:
                            traduzione=[]
                            for parola1 in parole[1:]:
                                traduzione.append(parola1)
                        self.dizionario[parola]=traduzione
        except FileNotFoundError:
            print("Nome file non valido")

    def addWord(self, coppia: str):
        coppia_divisa=coppia.strip().split()
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
        with open(self.nome_file, "w", encoding="utf-8") as f: #sovrascrivo l'intero file
            for (p, trad) in self.dizionario.items():
                riga=p
                for t in trad:
                    riga+=f" {t} "
                f.write(riga+"\n\n")
        #non devo chiudere il file perché il blocco with lo fa in automatico

    def translate(self, parola: str):
        return self.dizionario.get(parola.lower())

    def translateWordWildCard(self, word:str, index:int): #word è già depurata del carattere ?
        traduzioniW={}
        for k in self.dizionario.keys():
            key=k[:index]+k[index+1:] #non posso usare pop o remove perché le stringhe sono IMMUTABILI
            if key==word.lower():
                traduzioniW[k]=self.dizionario.get(k)
        return traduzioniW

