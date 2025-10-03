def feladat_1():
    # Írasd ki 3-szor a korábban bekért szöveget! (kedvenc együttes pl.)
    #   a: A bekért szöveg legyen legalább 3 karakteres! (ellenőrzött bekérés)

    bekeres = ""
    while not len(bekeres) >= 3:
        bekeres = input("Add meg a kedvenc egggyütttessed: ")

    for i in range(3):
        print(bekeres)

def feladat_2():
    # Kérj be ellenőrzötten egy számot 1 és 5 között, majd ennyi *-ot jeleníts meg szóközökkel elválasztva!

    szam = 0
    while not 1 <= szam <= 5:
        szam = int(input("Adj meg egy számot: "))

    for i in range(szam-1):
        print("* ", end="")
    print("*")
    
def feladat_3():
    # Írasd ki a számokat egyesével 0-tól 20-ig! (a 20-at is!)

    for i in range(0, 21):
        print(i)
        
def feladat_4():
    # Írasd ki a számokat kettesével 20-tól 56-ig! (az 56-ot is!)

    for i in range(20, 57, 2):
        print(i)
        
def feladat_5():
    # Írasd ki a számokat 4-esével 77-től -77-ig! 

    for i in range(77, -77, -4):
        print(i)
        
def feladat_6():
    # Kérj be 2 számot, majd írasd ki a számokat a legkisebbtől a legnagyobbig! (a legnagyobbat is! Ha az első szám nagyobb, abban az esetben is a legkisebbtől a legnagyobbig írasd ki!)

    a, b = input("Írj be két számot (pl: 0 5):").split()

    a = int(a)
    b = int(b)

    if b < a:
        a, b = b, a

    for i in range(a, b+1):
        print(i)
        
def feladat_7():
    # Kérj be 2 számot, majd írasd ki a számokat 0-tól a 2 szám szorzatáig!

    a, b = input("Írj be két számot (pl: 0 5):").split()

    a = int(a)
    b = int(b)

    szorzat = a * b

    for i in range(szorzat+1):
        print(i)
        
def feladat_8():
    # Írd meg a fenti feladatot while és for ciklussal is!

    a, b = input("Írj be két számot (pl: 0 5):").split()

    a = int(a)
    b = int(b)

    szorzat = a * b

    i = 0

    while i < szorzat+1:
        print(i)
        i += 1

def feladat_9():
    # Írasd ki az első 7 pozitív egész számot vesszővel elválasztva!
    #   A: úgy, hogy a végén ne legyen vessző!
    ...
