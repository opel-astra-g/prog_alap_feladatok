import math

PI = math.pi

def kor_sugar(hatar=0):
    """Ellenrzött bekérése egy határ alapján."""
    #A program olvasson be a konzolról addig egy valós számot (kör sugarát), 
    #amíg pozitív nem lesz! Majd számítsa ki és írja ki a kör kerületét,
    #területét a konzolra! Használj konstans-t a Pi használatára (kerekítsd az eredményt 3 tizedes jegyre)!

    bekeres = float(input("Adj meg egy pozitív valós számot:\n>"))
    while not bekeres > hatar:
        bekeres = float(input("Hiba! Adj meg egy pozitív valós számot:\n>"))

    return bekeres

def kor_kerulet(sugar:float) -> float:
    PI_LOCAL = PI
    return sugar*2*PI_LOCAL

def kor_terulet(sugar:float) -> float:
    PI_LOCAL = PI
    #return sugar*sugar*PI_LOCAL
    return sugar**2*PI_LOCAL

def kor_teljes_print(sugar):
    print(f"Kör sugara: {sugar}\nKör kerülete: {kor_kerulet(sugar):.1f}\nKör területe: {kor_terulet(sugar):.1f}")