# Cím;Rendező;Főszereplő;Év;Perc

class Film:
    def __init__(self, cim:str, rendezo:str, foszereplo:str, ev:int, perc:int):
        self.cim = cim
        self.rendezo = rendezo
        self.foszereplo = foszereplo
        self.ev = int(ev)
        self.perc = int(perc)
    def __str__(self):
        return f"Cím: {self.cim}\nRendező: {self.rendezo}\nFőszereplő: {self.foszereplo}\nÉv: {self.ev}\nPerc: {self.perc}"