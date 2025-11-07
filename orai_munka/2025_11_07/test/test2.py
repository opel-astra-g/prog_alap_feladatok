lista = ["páros", "páratlan"]

loop = True

while loop:
    try:
        print(f"A számod {lista[int(input(">")) % 2]}")
        loop = False
    except:
        print("Csak számok!")