# Find the sum of elements in an array
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Test
print(sum_array([1, 2, 3, 4]))  # Output: 10
