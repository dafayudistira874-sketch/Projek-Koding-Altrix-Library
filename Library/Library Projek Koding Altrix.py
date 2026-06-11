class Dafa084:

    @staticmethod
    def tampilkan(matriks):
        for baris in matriks:
            print(baris)

    @staticmethod
    def tambah(A, B):
        hasil = []
        for i in range(len(A)):
            baris = []
            for j in range(len(A[0])):
                baris.append(A[i][j] + B[i][j])
            hasil.append(baris)
        return hasil

    @staticmethod
    def kurang(A, B):
        hasil = []
        for i in range(len(A)):
            baris = []
            for j in range(len(A[0])):
                baris.append(A[i][j] - B[i][j])
            hasil.append(baris)
        return hasil

    @staticmethod
    def kali_skalar(A, k):
        hasil = []
        for baris in A:
            hasil.append([elemen * k for elemen in baris])
        return hasil

    @staticmethod
    def transpose(A):
        hasil = []
        for j in range(len(A[0])):
            baris = []
            for i in range(len(A)):
                baris.append(A[i][j])
            hasil.append(baris)
        return hasil

    @staticmethod
    def kali_matriks(A, B):
        hasil = []
        for i in range(len(A)):
            baris = []
            for j in range(len(B[0])):
                jumlah = 0
                for k in range(len(B)):
                    jumlah += A[i][k] * B[k][j]
                baris.append(jumlah)
            hasil.append(baris)
        return hasil

    @staticmethod
    def determinan_2x2(A):
        return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])

    @staticmethod
    def invers_2x2(A):
        det = Dafa084.determinan_2x2(A)

        if det == 0:
            return "Matriks tidak memiliki invers"

        return [
            [A[1][1] / det, -A[0][1] / det],
            [-A[1][0] / det, A[0][0] / det]
        ]