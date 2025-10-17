def egyes():
    szam = int(input("Írj be egy számot: "))
    while not (1 <= szam <= 9):
        szam = int(input("Írj be egy számot: "))
    return szam

def kettes():
    forditva = ""
    szo = input("Írj be egy szót: ")
    for i in range(-1, -len(szo)-1, -1):
        forditva += szo[i]
    return forditva

def kettes_parameter(szo: str):
    forditva = ""
    for i in range(-1, -len(szo)-1, -1):
        forditva += szo[i]
    return forditva