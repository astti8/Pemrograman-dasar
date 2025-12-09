#Contoh perancangan array 1D
#Tujuan : menyimpan 5 nilai siswa
#Tipe data : integer
#Ukuran : 5

nilai = [0] * 5  # array berukuran 5

for i in range(5):
    nilai[i] = int(input(f"Masukkan nilai ke-{i+1}: "))

print("Data nilai:", nilai)
