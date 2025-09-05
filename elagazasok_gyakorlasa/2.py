# A program  olvasson be a konzolról egy valós számot! A program számítsa ki a szám abszolút értékét, és írja ki az eredményeket a konzolra! A számításhoz függvény helyett elágazást használj!

szam = float(input("Írj be egy számot: "))

if szam < 0:
    abszolut = -szam
else:
    abszolut = szam

# abszolut = abs(szam)      függvénnyel

print(abszolut)
