# Írd meg a leghatékonyabb változatát 2 bekért szám növekvő sorrendbe tételének (az értékek legyenek növekvő sorrendben)! Pl. A = 6, B = 3 esetén az átalakítás után A értéke 3, B értéke 6 lesz. (Próbáld megoldani maximum 7 sorral!)

a = float(input("Írd be az első számot: "))
b = float(input("Írd be a második számot: "))

#if a > b:          chatgpt hatékonyabb megoldás
#   a, b = b, a

if a > b:
    extra = b
    b = a
    a = extra

print(f"A: {a}, B: {b}")