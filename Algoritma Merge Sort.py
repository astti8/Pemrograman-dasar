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