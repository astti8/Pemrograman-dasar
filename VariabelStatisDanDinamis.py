#Variabel Statis
def hitung():
    if not hasattr(hitung, "counter"):
        hitung.counter = 0
    hitung.counter += 1
    print("Dipanggil", hitung.counter, "kali")
hitung()
hitung()
hitung()

#Variabel Dinamis
data = []          # list kosong (dinamis)
data.append(10)    # tambah data
data.append(20)
data.append("Asti")

print(data)