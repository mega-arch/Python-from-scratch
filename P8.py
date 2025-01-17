# Implement Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if target is found
    return -1  # Return -1 if target is not found

# Test
print(linear_search([10, 20, 30, 40], 30))  # Output: 2
