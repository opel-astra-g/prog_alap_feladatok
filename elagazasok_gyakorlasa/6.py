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