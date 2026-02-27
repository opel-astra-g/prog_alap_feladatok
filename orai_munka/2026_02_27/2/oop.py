import osztaly

def beolvasas():
    f = open("tizedik.txt", "r", encoding="utf8")
    f.readline
    sorok = f.readlines()
    f.close()

    diakok = []

    for i in range(len(sorok)):
        darabok = sorok[i].split("/")
        diak = osztaly.Diak(darabok[0], darabok[1], darabok[2])
        diakok.append(diak)

    return diakok
