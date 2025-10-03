def feladat_1():
    # A program olvasson be a konzolról egy egész számot! A program döntse el, hogy a megadott szám páros vagy páratlan, és írja ki az eredményt a konzolra!

    szam = int(input("Írj be egy egész számot: "))

    if szam % 2 == 0:
        print("páros")
    else:
        print("páratlan")

def feladat_2():
    # A program  olvasson be a konzolról egy valós számot! A program számítsa ki a szám abszolút értékét, és írja ki az eredményeket a konzolra! A számításhoz függvény helyett elágazást használj!

    szam = float(input("Írj be egy számot: "))

    if szam < 0:
        abszolut = -szam
    else:
        abszolut = szam

    # abszolut = abs(szam)      függvénnyel

    print(abszolut)

def feladat_3():
    # A program  olvasson be a konzolról egy valós számot! A program számítsa ki a szám abszolút értékét, és írja ki az eredményeket a konzolra! A számításhoz függvény helyett elágazást használj!

    szam = float(input("Írj be egy számot: "))

    if szam < 0:
        abszolut = -szam
    else:
        abszolut = szam

    # abszolut = abs(szam)      függvénnyel

    print(abszolut)

def feladat_4():
    # A program olvassa be a konzolról egy kör sugarát! Ha a sugár nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kör sugara nem pozitív!"; egyébként a program számítsa ki és írja ki a kör kerületét, területét a konzolra!

    sugar = float(input("Írd be a kör sugarát: "))

    if sugar > 0:
        kerulet = 2*sugar*3.14
        terulet = (sugar*sugar)*3.14

        print(f"Kerület: {kerulet}, Terület: {terulet}")
    else:
        print("Hiba: a kör sugara nem pozitív")

def feladat_5():
    # Kérj be egy nevet és egy egész számot (kor)! Ha az illető Ferenc, vagy kiskorú, akkor üdvözöljük úgy, hogy Kedves plusz a neve, pl. így: “Kedves Péter!” Ha 65 év feletti (és nem Ferenc), akkor Tisztelt plusz a név! Egyéb esetben írja ki, hogy Helló plusz a név!

    nev = input("Írja be a nevét: ")
    kor = int(input("Írja be a korát: "))

    if nev == "Ferenc" or kor < 18:
        print(f"Kedves {nev}!")
    elif nev != "Ferenc" and kor > 65:
        print(f"Tisztelt {nev}!")
    else:
        print(f"Helló {nev}!")

def feladat_6():
    # A program olvasson be a konzolról egy egész számot! Ha a szám pozitív, akkor legyen a beolvasott szám egy méterben kifejezett tengerszint feletti magasság. Ha a magasság 200 m alatti, akkor "Alföld", egyébként, ha 500 m alatti, akkor "Dombság", egyébként, ha 1500 m alatti, akkor "Középhegység", egyébként "Hegység"-ről van szó! A program írja ki a megfelelő szöveget a konzolra!

    magassag = int(input("Írj be egy számot: "))

    if magassag < 200:
        print("Alföld")
    elif magassag < 500:
        print("Dombság")
    elif magassag < 1500:
        print("Középhegység")
    else:
        print("Hegység")

def feladat_7():
    print("Az egyenlet: a*x+b=0")

    a = float(input("Írd be az A értéket:>\n"))
    b = float(input("Írd be a B értéket:\n>"))

    if a != 0:
        x = (-1*b)/a

        print(f"Az X {x}")
    elif b == 0:
        print("X bármilyen valós szám")
    else:
        print("Az A érték nem lehet nulla, nincs megoldás")

def feladat_8():
    # A program kérjen be egy évszámot a felhasználótól! Ha ez 1900 és 2099 közé esik, akkor a program írja ki, hogy az adott évben melyik napra esik húsvét vasárnap - a Gergely naptár szerint! A kiszámítás algoritmusa (Gauss módszer): https://hu.wikipedia.org/wiki/H%C3%BAsv%C3%A9tsz%C3%A1m%C3%ADt%C3%A1s#Gauss_m%C3%B3dszere

    evszam = int(input("Írd be az évszámot: "))

    if 1900 <= evszam <= 2099:
        a = evszam % 19
        b = evszam % 4
        c = evszam % 7

        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7

        if d + e < 10:
            print(f"Március {d + e + 22}")
        else:
            april = d + e - 9
            if april == 26:
                print(f"Április 19")
            elif april == 25:
                print(f"Április 18")
            else:
                print(f"Április {april}")

def osszetett_feladat_1():
    temperature = float(input("Add meg a hőmérsékletet\n>"))
    kontinens = int(input("Add meg a számod: (1: Afrika, 2: Ausztrália, 3: Európa, 4: Ázsia, 5: Amerika)\n>"))

    if temperature > 38 and 3 <= kontinens <= 5:
        print("Hőségriadó!")
    if temperature < 15 and 1 <= kontinens <= 2:
        print("Hideg van!")

def osszetett_feladat_2():
    temperature = float(input("Add meg a hőmérsékletet (celsius)\n>"))
    kontinens = int(input("Add meg a számod (1: Afrika, 2: Ausztrália, 3: Európa, 4: Ázsia, 5: Amerika)\n>"))
    evszam = int(input("Írj be egy évszámot\n>"))

    if temperature > 38 and 3 <= kontinens <= 5:
        print("Hőségriadó!")
        if kontinens == 5 and evszam > 1700:
            print(f"Fahrenheit: {temperature*1.8}")
        if temperature < 15 and 1 <= kontinens <= 2:
            print("Hideg van!")
    
def osszetett_feladat_3():
    # A bemenő számokat az alábbi csoportba tudjuk tenni:
    # A: Páros, [-100,100] tartományban van, vagy
    # B: Páratlan, [-200, 200] tartományban, vagy 
    # C: egyik sem igaz rá.
    # Írasd ki a fentiek alapján a bemenő számra melyik csoport vonatkozik!

    bemenet = float(input("Add meg a számot: "))

    if bemenet % 2 == 0 and -100 <= bemenet <= 100:
        print("A")
    elif bemenet % 2 == 1 and -200 <= bemenet <= 200:
        print("B")
    else:
        print("C")

def osszetett_feladat_4():
    a, b = input("Írd be az A és B értéket (pl: 5 4)\n>").split()

    terulet = int(a) * int(b)
    kerulet = 2*(int(a) + int(b))

    atlag = False

    if terulet < 100 and kerulet < 100:
        print("Kis téglalap")
        atlag = True
    if int(a) == int(b):
        print("A téglalap egy négyzet")
        atlag = True
    if int(a) < int(b)/3 or int(b) < int(a)/3:
        print("A téglalap keskeny")
        atlag = True
    if atlag == 0:
        print("Ez egy normális téglalap")