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