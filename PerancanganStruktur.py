#Contoh perancangan Struktur (struktur mahsaiswa)

#Struktur Mahasiswa:
#    nama: string
#    nim: string
#    umur: int

class Mahasiswa:
    def __init__(self, nama, nim, umur):
        self.nama = nama
        self.nim = nim
        self.umur = umur

m1 = Mahasiswa("Asti", "D0425326", 17)
print(m1.nama, m1.nim, m1.umur)

