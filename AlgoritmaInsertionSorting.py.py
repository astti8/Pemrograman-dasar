def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]          # Elemen yang ingin disisipkan
        j = i - 1

        # Geser elemen yang lebih besar ke kanan
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Tempatkan key pada posisi yang tepat
        arr[j + 1] = key

    return arr

data = [12, 11, 13, 5, 6]
print("Sebelum sorting:", data)
print("Setelah sorting:", insertion_sort(data))