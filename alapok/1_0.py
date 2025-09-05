# Kérj be 3 számot, majd írasd ki azt, hogy “Van egyenlő a számok között!”, ha ez igaz állítás, és “Nincs egyenlő a számok között!”, ha utóbbi az igaz állítás!

number_1 = float(input("Írd be az első számot: "))
number_2 = float(input("Írd be a második számot: "))
number_3 = float(input("Írd be a harmadik számot: "))

if number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
    print("Van egyenlő a számok között!")
else:
    print("Nincs egyenlő a számok között!")