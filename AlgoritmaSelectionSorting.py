def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Anggap elemen pertama dari sisa array adalah yang terkecil
        min_index = i

        # Cari elemen terkecil di sisa array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Tukar elemen terkecil dengan arr[i]
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Contoh pemakaian
data = [64, 25, 12, 22, 11]
print("Sebelum sorting:", data)
print("Setelah sorting:", selection_sort(data))
