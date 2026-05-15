import random


class Matrix:
    def __init__(self, sor, oszlop):
        self._sor = sor
        self._oszlop = oszlop
        self._lista = self.feltolt()

    def feltolt(self):
        lista = []
        for i in range(self._sor):
            sorok = []
            for j in range(self._oszlop):
                sorok.append(random.randint(0, 9))
            lista.append(sorok)
        return lista

    def kiir_matrix(self):
        for i in range(self._sor):
            print(self._lista[i])

    def kigyo(self):
        for i in range(self._oszlop):
            if i % 2 == 0:
                self.fuggoleges_kiir(i, range(0, self._sor, 1))
            else:
                self.fuggoleges_kiir(i, range(self._sor-1, -1, -1))

    def fuggoleges_kiir(self, akt_oszlop, sor_range):
        for i in sor_range:
            print(f"\033[31m{self._lista[i][akt_oszlop]}\033[0m", end=" ")

    def vizszintes_kiir(self, akt_sor, sor_range):
        for i in sor_range:
            print(f"\033[32m{self._lista[akt_sor][i]}\033[0m", end=" ")

    def spiral(self):
        kezdo_sor = 0
        kezdo_oszlop = 0
        hatar_sor = self._sor
        hatar_oszlop = self._oszlop

        elem_mennyiseg = self._sor * self._oszlop
        hany_elem = 0

        while not(hany_elem == elem_mennyiseg):
            if kezdo_sor < hatar_sor:
                self.fuggoleges_kiir(kezdo_oszlop, range(0, hatar_sor, 1))
                for i in range(0, hatar_sor, 1): hany_elem += 1

                kezdo_sor = hatar_sor
                hatar_sor -= 1
            
            # fel
            # bal

            

