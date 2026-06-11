from Dafa084 import Dafa084

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print("Penjumlahan Matriks:")
Dafa084.tampilkan(Dafa084.tambah(A, B))

print("\nPerkalian Matriks:")
Dafa084.tampilkan(Dafa084.kali_matriks(A, B))

print("\nTranspose Matriks A:")
Dafa084.tampilkan(Dafa084.transpose(A))

print("\nDeterminan Matriks A:")
print(Dafa084.determinan_2x2(A))

print("\nInvers Matriks A:")
Dafa084.tampilkan(Dafa084.invers_2x2(A))