import random

# lista készítése valós véletlen számok
# mérete a paraméter
# átlagszámítás
# negatív és páros számok megszámlálása
# legkisebb szám és a helye (felh barát módon)

def lista_keszites(hossz: int) -> list[float]:
    tortek = []
    for i in range(hossz):
        tortek.append(round(random.random() * 20 - 10, 2))
    return tortek

def atlag_szamitas(list):
    return lista_elem_osszeadas(list) / lista_hossz(list)

def lista_hossz(list):
    hossz = 0
    for _ in list:
        hossz += 1
    return hossz

def lista_elem_osszeadas(list):
    osszeg = 0
    for i in range(lista_hossz(list)):
        osszeg += list[i]
    return osszeg

def elem_szamlalas(paros: bool, pozitiv:bool, list):
    db = 0
    for elem in list:
        if paros and elem % 2 == 0: #ha párost keresünk
            if pozitiv and elem >= 0: #ha pozitív párost keresünk
                db += 1
            elif not(pozitiv) and elem < 0: # ha negatív párost keresünk
                db += 1
        elif not(paros) and not(elem % 2 == 0): #ha páratlant keresünk
            if pozitiv and elem >= 0: #ha pozitív páratlan keresünk
                db += 1
            elif not(pozitiv) and elem < 0: # ha negatív páratlan keresünk
                db += 1
    return db

def teljes():
    lista = lista_keszites(10)
    atlag = atlag_szamitas(lista)
    megszamlalas = elem_szamlalas(True, False, lista)
    

if __name__ == "__main__":
    teljes()