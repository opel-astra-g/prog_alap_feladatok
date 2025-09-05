# A program olvassa be a konzolról egy kör sugarát! Ha a sugár nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kör sugara nem pozitív!"; egyébként a program számítsa ki és írja ki a kör kerületét, területét a konzolra!

sugar = float(input("Írd be a kör sugarát: "))

if sugar > 0:
    kerulet = 2*sugar*3.14
    terulet = (sugar*sugar)*3.14

    print(f"Kerület: {kerulet}, Terület: {terulet}")
else:
    print("Hiba: a kör sugara nem pozitív")