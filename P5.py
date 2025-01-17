# Find the index of the first occurrence of an element
def find_index(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1  # Return -1 if the element is not found

# Test
print(find_index([10, 20, 30, 40], 30))  # Output: 2
