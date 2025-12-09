#SHELL SHORT
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    # Loop sampai gap menjadi 0
    while gap > 0:
        # Lakukan insertion sort versi gap
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Geser elemen yang lebih besar ke depan
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

        # Perkecil gap
        gap //= 2

    return arr

# Contoh penggunaan
data = [45, 23, 53, 12, 9, 87, 34]
print("Sebelum sorting:", data)
print("Setelah sorting:", shell_sort(data))


#MERGE SORT
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Bagi array menjadi dua bagian
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge dua bagian terurut
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Bandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Tambahkan sisa elemen
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Contoh penggunaan
data = [38, 27, 43, 3, 9, 82, 10]
print("Sebelum sorting:", data)
print("Setelah sorting:", merge_sort(data))


#QUICT SORT
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # ambil pivot dari tengah
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

data = [33, 10, 55, 26, 17, 89, 42]
print("Sebelum sorting:", data)
print("Setelah sorting:", quick_sort(data))
