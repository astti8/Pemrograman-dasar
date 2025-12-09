#Struktur merupakan kumpulan variabel dengan tipe berbeda yang digabung menjadi satu objek

class Mahasiswa:
    def __init__(self, nama, nim, umur):
        self.nama = nama
        self.nim = nim
        self.umur = umur

# membuat objek
m1 = Mahasiswa("Asti", "D0425326", 17)
m2 = Mahasiswa("Juju", "D0294829", 20)

print("Nama:", m2.nama)
print("NIM:", m2.nim)
print("Umur:", m2.umur)