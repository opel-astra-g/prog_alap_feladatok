def fileba_ir():
    f = open("proba.txt", "w", encoding="utf8")
    f.write("Micó")
    f.write("\nMokus")
    f.close()

def file_olvasas():
   for i in range(3):
        f = open("proba.txt", "r", encoding="utf8")
        if i == 0:
            print(f.read())
        elif i == 1:
            print(f.read(3))
        else:
            print(f.readlines()[1])
        f.close()