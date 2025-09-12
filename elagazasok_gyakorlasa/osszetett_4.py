a, b = input("Írd be az A és B értéket (pl: 5 4)\n>").split()

terulet = int(a) * int(b)
kerulet = 2*(int(a) + int(b))

atlag = False

if terulet < 100 and kerulet < 100:
    print("Kis téglalap")
    atlag = True
if int(a) == int(b):
    print("A téglalap egy négyzet")
    atlag = True
if int(a) < int(b)/3 or int(b) < int(a)/3:
    print("A téglalap keskeny")
    atlag = True
if atlag == 0:
    print("Ez egy normális téglalap")