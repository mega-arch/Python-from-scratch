# Implement Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:  # Shift elements to the right
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Place the key at the correct position
    return arr

# Test
print(insertion_sort([12, 11, 13, 5, 6]))  # Output: [5, 6, 11, 12, 13]
