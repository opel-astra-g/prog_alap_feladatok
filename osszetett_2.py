temperature = float(input("Add meg a hőmérsékletet (celsius)\n>"))
kontinens = int(input("Add meg a számod (1: Afrika, 2: Ausztrália, 3: Európa, 4: Ázsia, 5: Amerika)\n>"))
evszam = int(input("Írj be egy évszámot\n>"))

if temperature > 38 and 3 <= kontinens <= 5:
    print("Hőségriadó!")
    if kontinens == 5 and evszam > 1700:
        print(f"Fahrenheit: {temperature*1.8}")
if temperature < 15 and 1 <= kontinens <= 2:
    print("Hideg van!")