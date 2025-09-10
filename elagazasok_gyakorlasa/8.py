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