#Nama : Asti
#NIM : D0425326
#Materi : Dictionary

Data_mahasiswa = {
    "nama" : "Asti", 
    "umur" : 17,
}
#menambah data
Data_mahasiswa ["fakultas"] = "Teknik"
#menghapus data
del Data_mahasiswa ["umur"]
#mengubah data
Data_mahasiswa ["umur"] = 18
#percabangan
if "alamat" in Data_mahasiswa :
    print ("data lengkap")
else :
    print ("data tidak lengkap")
#menghitung data
print (len(Data_mahasiswa))
print (Data_mahasiswa) 