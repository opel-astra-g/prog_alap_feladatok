def feladat_1_0():
    # Kérj be 3 számot, majd írasd ki azt, hogy “Van egyenlő a számok között!”, ha ez igaz állítás, és “Nincs egyenlő a számok között!”, ha utóbbi az igaz állítás!

    number_1 = float(input("Írd be az első számot: "))
    number_2 = float(input("Írd be a második számot: "))
    number_3 = float(input("Írd be a harmadik számot: "))

    if number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
        print("Van egyenlő a számok között!")
    else:
        print("Nincs egyenlő a számok között!")

def feladat_1_1():
    # A program két valós beolvasott számot összehasonlítva írja közéjük a megfelelő relációs jelet (<, >, =)! pl. Be: 4.5, 7, Ki: 4.5 < 7

    # kettő egyes feladat van a python alapok google documentumban ezért van itt is kettő

    number_1 = float(input("Írd be az első számot: "))
    number_2 = float(input("Írd be a második számot: "))

    matek_szimbolum = ""

    if number_1 < number_2:
        matek_szimbolum = "<"
    elif number_1 > number_2:
        matek_szimbolum = ">"
    else:
        matek_szimbolum = "="

    print(number_1, matek_szimbolum, number_2)

def feladat_2():
    # Egy 100 pontos dolgozatot alapul véve írasd ki a szerinted igazságos pontozás és a bekért szám (mint eredmény) alapján, hogy jeles, jó, közepes, elégséges vagy elégtelen a dolgozat!

    pontok = int(input("Írd be a dolgozat pontszámát: "))

    if 0 <= pontok <= 39:
        print("Elégtelen")
    elif 40 <= pontok <= 59:
        print("Elégséges")
    elif 60 <= pontok <= 74:
        print("Közepes")
    elif 75 <= pontok <= 89:
        print("Jó")
    elif 90 <= pontok <= 100:
        print("Jeles")

def feladat_3():
    # A program kérjen be egy egész számot (dolgozat jegye), és ez alapján írasd ki a hozzá tartozó értékelést! Az alapértelmezés az elégtelen. (match-case)

    jegy = int(input("Írd be a dolgozat jegyét: "))

    if jegy == 5:
        print("Jeles")
    elif jegy == 4:
        print("Jó")
    elif jegy == 3:
        print("Közepes")
    elif jegy == 2:
        print("Elégséges")
    else:
        print("Elégtelen")

def feladat_4():
    # A program kérjen be a konzolról egy egész számot! Ha a szám egyjegyű, akkor a program írja ki a konzolra a számot megelőző és követő egész számot, egyébként ne írjon ki semmit!

    szam = int(input("Írj be egy egész számot: "))

    elotte = szam - 1
    utana = szam + 1

    if len(str(szam)) == 1:
        print(elotte, utana)

def feladat_5():
    # Írd meg a leghatékonyabb változatát 2 bekért szám növekvő sorrendbe tételének (az értékek legyenek növekvő sorrendben)! Pl. A = 6, B = 3 esetén az átalakítás után A értéke 3, B értéke 6 lesz. (Próbáld megoldani maximum 7 sorral!)

    a = float(input("Írd be az első számot: "))
    b = float(input("Írd be a második számot: "))

    #if a > b:          chatgpt hatékonyabb megoldás
    #   a, b = b, a

    if a > b:
        extra = b
        b = a
        a = extra

    print(f"A: {a}, B: {b}")

def feladat_6():
    ...