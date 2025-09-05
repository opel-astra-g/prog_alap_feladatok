print("Az egyenlet: a*x+b=0")

a = float(input("Írd be az A értéket:>\n"))
b = float(input("Írd be a B értéket:\n>"))

if a != 0:
    x = (-1*b)/a

    print(f"Az X {x}")
elif b == 0:
    print("X bármilyen valós szám")
else:
    print("Az A érték nem lehet nulla, nincs megoldás")