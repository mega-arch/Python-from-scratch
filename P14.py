# Merge two arrays
def merge_arrays(arr1, arr2):
    merged = []
    for num in arr1:
        merged.append(num)
    for num in arr2:
        merged.append(num)
    return merged

# Test
print(merge_arrays([1, 2, 3], [4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]
