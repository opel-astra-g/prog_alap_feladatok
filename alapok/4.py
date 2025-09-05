# A program kérjen be a konzolról egy egész számot! Ha a szám egyjegyű, akkor a program írja ki a konzolra a számot megelőző és követő egész számot, egyébként ne írjon ki semmit!

szam = int(input("Írj be egy egész számot: "))

elotte = szam - 1
utana = szam + 1

if len(str(szam)) == 1:
    print(elotte, utana)