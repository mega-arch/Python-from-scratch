# Check if an element is in the array
def element_in_array(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return True
    return False

# Test
print(element_in_array([1, 2, 3, 4], 3))  # Output: True
