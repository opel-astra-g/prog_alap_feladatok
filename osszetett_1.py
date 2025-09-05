temperature = float(input("Add meg a hőmérsékletet\n>"))
kontinens = int(input("Add meg a számod: (1: Afrika, 2: Ausztrália, 3: Európa, 4: Ázsia, 5: Amerika)\n>"))

if temperature > 38 and 3 <= kontinens <= 5:
    print("Hőségriadó!")
if temperature < 15 and 1 <= kontinens <= 2:
    print("Hideg van!")