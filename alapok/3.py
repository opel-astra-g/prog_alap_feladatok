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