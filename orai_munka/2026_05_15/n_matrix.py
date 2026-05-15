from matrix import Matrix

class NMatrix(Matrix):
    def __init__(self, sor):
        super().__init__(sor, sor)

    def bal_le_a_also(self, akt_sor):
        ...

    def bal_le_a_felso(self, akt_oszlop):
        ...

    """def atlo_max(self, atlo_fv, kezdo_index=0):
        maximum = 0
        for i in range(kezdo_index, len(self._lista)):
            ertek = atlo_fv(i)
            if ertek > maximum:
                maximum = ertek
        return maximum"""

    def b_l_a_max(self):
        return max(self.bal_le_a_also(i) for i in range(self._sor))

    def b_l_f_max(self):
        return max(self.bal_le_a_felso(i) for i in range(1, self._sor))
        # return self.atlo_max(self.bal_le_a_felso, 1)

