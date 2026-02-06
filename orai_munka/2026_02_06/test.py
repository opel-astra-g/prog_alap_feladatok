def elem_szamlalas(paros: bool, pozitiv:bool, list):
    db = 0
    for elem in list:
        if paros and elem % 2 == 0: #ha párost keresünk
            if pozitiv and elem >= 0: #ha pozitív párost keresünk
                db += 1
            elif not(pozitiv) and elem < 0: # ha negatív párost keresünk
                db += 1
        elif not(paros) and not(elem % 2 == 0): #ha páratlant keresünk
            if pozitiv and elem >= 0: #ha pozitív páratlan keresünk
                db += 1
            elif not(pozitiv) and elem < 0: # ha negatív páratlan keresünk
                db += 1
    print(db)

lista = [1, 1.1, 1.5, 2, 5.3, 6, 8, -1, -1.1, -1.5, -2]

elem_szamlalas(False, False, lista)