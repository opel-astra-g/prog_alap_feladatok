a, b = input("Írd be az A és B értéket (pl: 5 4)\n>").split()

terulet = int(a) * int(b)
kerulet = 2*(int(a) + int(b))

atlag = 0

if terulet < 100 and kerulet < 100:
    print("Kis téglalap")
    atlag += 1
if int(a) == int(b):
    print("A téglalap egy négyzet")
    atlag += 1
if int(a) < int(b)/3 or int(b) < int(a)/3:
    print("A téglalap keskeny")
    atlag += 1
if atlag == 0:
    print("Ez egy normális téglalap")