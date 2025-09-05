# A program két valós beolvasott számot összehasonlítva írja közéjük a megfelelő relációs jelet (<, >, =)! pl. Be: 4.5, 7, Ki: 4.5 < 7

# kettő egyes feladat van a python alapok google documentumban ezért van itt is kettő

number_1 = float(input("Írd be az első számot: "))
number_2 = float(input("Írd be a második számot: "))

matek_szimbolum = ""

if number_1 < number_2:
    matek_szimbolum = "<"
elif number_1 > number_2:
    matek_szimbolum = ">"
else:
    matek_szimbolum = "="

print(number_1, matek_szimbolum, number_2)