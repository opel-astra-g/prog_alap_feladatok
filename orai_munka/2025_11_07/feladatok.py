import random

def feladat1():
    bemenet = input("Szó: ")
    while not (bemenet == "vége"):
        bemenet = input("Szó: ")

def feladat2():
    #Kérj be szavakat, amíg a felhasználó nem írja be, hogy „vége”. Írd ki a leghosszabb szót, amit beírt (A len függvény segít)
    bemenet = input("Szó: ")
    elozo = ""

    while not (bemenet == "vége"):
        bemenet = input("Szó: ")

        if len(bemenet) > len(elozo) and bemenet != "vége":
            elozo = bemenet

    print(elozo)

def feladat3():
    #Generáltass 10 véletlen kockadobás értéket (1–6 között véletlenszám), és írasd ki a legnagyobb dobás értékét.
    big = 0
    for i in range(10):
        ran = random.randint(1, 6)
        print(ran, end=" ")
        if ran > big:
            big = ran

    print(f"\nnagy: {big}")

def feladat4():
    #Ismételj meg 8-szor egy fej-írás dobás-szimulációt, és írd ki az eredményeket egymás mellé.
    print("Eredmények:")
    for i in range(8):
        ertek = random.randint(0, 1)
        print("Fej") if ertek else print("Írás")

def feladat5():
    #Kérj be n db egész számot (az n értékét előtte olvasd be), és számold ki az összegüket.
    n = int(input("Hány darab számot kérjen be: \n>"))
    osszeg = 0
    for i in range(n):
        osszeg += int(input("Írd be az egész számot: \n>"))
    print("Összeg: ", osszeg)

def feladat6():
    #fenti csak while
    i = 0
    osszeg = 0
    bekeres = int(input("Hány darab szám: \n>"))
    while i < bekeres:
        osszeg += int(input("Írd be az egész számot: \n>"))
        i += 1
    print("Összeg: ", osszeg)