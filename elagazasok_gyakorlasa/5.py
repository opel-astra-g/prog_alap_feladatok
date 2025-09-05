# Kérj be egy nevet és egy egész számot (kor)! Ha az illető Ferenc, vagy kiskorú, akkor üdvözöljük úgy, hogy Kedves plusz a neve, pl. így: “Kedves Péter!” Ha 65 év feletti (és nem Ferenc), akkor Tisztelt plusz a név! Egyéb esetben írja ki, hogy Helló plusz a név!

nev = input("Írja be a nevét: ")
kor = int(input("Írja be a korát: "))

if nev == "Ferenc" or kor < 18:
    print(f"Kedves {nev}!")
elif nev != "Ferenc" and kor > 65:
    print(f"Tisztelt {nev}!")
else:
    print(f"Helló {nev}!")