import osztaly


def beolvasas():
    
    f = open("tizedikesek.txt", "r", encoding="utf8")
    # első sor eldobása
    f.readline()
    # maradék sorok listába
    sorok = f.readlines()
    f.close()
    return sorok

def obj_lista(sorok: list[str]):
    diakok = []
    for i in range(len(sorok)):
        darabok = sorok[i].split("/") #strip()
        diak = osztaly.Diak(nev=darabok[0], eletkor=darabok[1], atlag=darabok[2])
        diakok.append(diak)
    return diakok

def atlag(diakok):
    #atlag = []
    #for elem in diakok:
        #atlag.append(elem.atlag)
    #atlag = sum(atlag) / len(atlag)
    #return atlag
        
    osszeg = 0
    meret = len(diakok)
    for i in range(meret):
        osszeg += diakok[i].atlag
    return round(osszeg / meret, 2)

def eletkor_szamlalas(diakok, kor):
    db = 0
    for i in range(len(diakok)):
        if diakok[i].eletkor < kor:
            db += 1
    return db

def teljes():
    #print(beolvasas())
    sorok = beolvasas()
    print(sorok)
    diakok = obj_lista(sorok)
    print(diakok[0])
    print(atlag(diakok))
    print(eletkor_szamlalas(diakok, 18))