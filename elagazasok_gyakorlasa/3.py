# A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!

szam = float(input("Írj be egy számot: "))

if szam > 0:
    print(szam ** 0.5)
else:
    print("Csak pozitív számok!")