class Diak:
    def __init__(self, nev:str, eletkor:str, atlag:str):
        self.nev = nev
        self.eletkor = int(eletkor)
        self.atlag = float(atlag.replace(",", "."))