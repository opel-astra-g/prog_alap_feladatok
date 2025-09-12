# A bemenő számokat az alábbi csoportba tudjuk tenni:
# A: Páros, [-100,100] tartományban van, vagy
# B: Páratlan, [-200, 200] tartományban, vagy 
# C: egyik sem igaz rá.
# Írasd ki a fentiek alapján a bemenő számra melyik csoport vonatkozik!

bemenet = float(input("Add meg a számot: "))

if bemenet % 2 == 0 and -100 <= bemenet <= 100:
    print("A")
elif bemenet % 2 == 1 and -200 <= bemenet <= 200:
    print("B")
else:
    print("C")