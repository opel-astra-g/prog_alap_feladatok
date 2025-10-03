import random

def feladat_1(a=0, b=150):
    #Írjuk ki 0-tól 150-ig a páros számokat!
    # a: két bekért szám közötti számokra működjön! (alap esetben a második nagyobb, mint az első)
    # b: bármilyen sorrendben működjön!
    # c: bekért számok helyett paraméter legyen!
    # d: minden 5. után legyen sortörés

    sortores = 0

    if a > b:
        a, b = b, a

    if a % 2 == 1:
        a += 1

    for i in range(a, b+1, 2):  #for ciklus határozott, while nemtudjuk hánysor
        print(f"{i}", end=", ")
        if sortores == 4:
            print("")
            sortores = 0
        else:
            sortores += 1

def feladat_2():
    #Számold meg 10 bekért szám esetében a 3-mal osztható számokat!

    oszhatoak = 0

    for i in range(10):
        bekeres = float(input(f"Írd be a {i+1}-es számot: \n>"))

        if bekeres % 3 == 0:
            oszhatoak += 1
    print(f"{oszhatoak} szám osztható hárommal.")

def feladat_3():
    #Addig kérjünk be szám(ok)at, amíg 10-zel osztható nem lesz!
    # A: majd írass ki ennyi *-ot!

    bekeres = int(input("Írj be egy tízzel osztható számot: \n>"))
    while not bekeres % 10 == 0:
        bekeres = int(input("Írj be egy tízzel osztható számot: \n>"))
    print("*"*bekeres) 

def feladat_5():
    szam = int(input("Pozitív páratlan szám: "))
    while not (szam > 0 and szam % 2 == 1):
        szam = int(input("Hiba! Pozitív páratlan szám: "))

def feladat_7():
    # Kérj be valós 3 számot, amíg szerkeszthető háromszög oldalait nem kapjuk! 
    a=int(input("1.: "))
    b=int(input("2.: "))
    c=int(input("3.: "))
    while not (a+b>c and a+c>b and b+c>a):
        print("Hibás értékek. Ajd meg újakat.")
        a=int(input("1.: "))
        b=int(input("2.: "))
        c=int(input("3.: "))

def feladat_8():
    # Addig kérjünk be szöveget, amíg legalább 3 karakterest nem írnak be. Majd írjuk ki a szót csupa nagy betűvel!*

    szöveg = input("Írj be szöveget: ")
    while not len(szöveg) > 2:
        szöveg = input("Nem elég hosszú. Írj be új szöveget: ")
    print(szöveg.upper()) 

def feladat_9():
    # Addig kérjünk be szöveget, amíg csupa kis betűs és 4 karakteres szót nem adnak meg!*
    szöveg = input("Írj be szöveget: ")
    while not (len(szöveg) == 4 and szöveg.islower()):
        szöveg = input("Nem megfelelő hosszúság, vagy nem kisbetűk. ")
    

def feladat_10():
    db = 0
    for i in range(10):
        veletlen = random.randint(10, 20)
        print(veletlen, end=" ")
        if veletlen % 10 == 1:
            db = db + 1
    print(f"\nAz egyre végződő számok db száma: {db}")

def feladat_10_while():
    loop = 0
    db = 0
    while loop < 10:
        veletlen = random.randint(10, 20)
        print(veletlen, end=" ")
        if veletlen % 10 == 1:
            db = db + 1
        loop += 1
    print(f"\nAz egyre végződő számok db száma: {db}")

