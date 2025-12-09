def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

data = [12, 45, 23, 8, 19]
target = 23

posisi = linear_search(data, target)
print("Ditemukan di indeks:", posisi)