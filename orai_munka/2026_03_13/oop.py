import osztaly

def beolvasas():
    f = open("film.txt", "r", encoding="UTF8")
    f.readline()
    sorok = f.readlines()

    f.close()
    return sorok #lista

def obj_lista(sorok:list):
    filmek = []
    for elem in sorok:
        darabok = elem.split(";")
        film = osztaly.Film(cim=darabok[0], rendezo=darabok[1], foszereplo=darabok[2], ev=darabok[3], perc=darabok[4])
        filmek.append(film)
    return filmek

def sorok_szama(filmek):
    return len(filmek)

def legrovidebb_cim(filmek: list[osztaly.Film]) -> str:
    min_index = 0
    for i in range(1, len(filmek)):
        if filmek[i].perc < filmek[min_index].perc:
            min_index = i
    return filmek[min_index].cim

def teljes():
    sorok = beolvasas()
    filmek = obj_lista(sorok)
    print(sorok_szama(filmek))
    print(legrovidebb_cim(filmek))