# A program olvasson be a konzolról egy egész számot! A program döntse el, hogy a megadott szám páros vagy páratlan, és írja ki az eredményt a konzolra!

szam = int(input("Írj be egy egész számot: "))

if szam % 2 == 0:
    print("páros")
else:
    print("páratlan")