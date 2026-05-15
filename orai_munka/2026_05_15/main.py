import matrix, n_matrix

print("Mátrix")
m = matrix.Matrix(10,5)
m.kiir_matrix()

print("Kígyó")
m.kigyo()

print("\nSpirál")
m.spiral()

print("\nNégyzetes mátrix")
n = n_matrix.NMatrix(3)
n.kiir_matrix()
print("Bal-le átlók maximuma")
#print(max(n.b_l_f_max(), n.b_l_a_max()))
