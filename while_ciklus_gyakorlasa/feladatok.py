def feladat_1_while(a=0, b=150):
    #Írjuk ki 0-tól 150-ig a páros számokat!
    # a: két bekért szám közötti számokra működjön! (alap esetben a második nagyobb, mint az első)
    # b: bármilyen sorrendben működjön!
    # c: bekért számok helyett paraméter legyen!
    # d: minden 5. után legyen sortörés

    sortores = 0

    if a > b:
        a, b = b, a

    while a < b+1:
        if a % 2 == 0:
            print(f"{a}", end=", ")
            if sortores == 4:
                print("")
                sortores = 0
            else:
                sortores += 1
        a += 1

def feladat_1_for(a=0, b=150):
    #ugyanaz a feladat mint a fenti csak egy for-ral

    sortores = 0

    if a > b:
        a, b = b, a

    if a % 2 == 1:
        a += 1

    for i in range(a, b+1, 2):
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