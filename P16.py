# Find missing values in a dataset (list of lists or 2D array)
def find_missing_values(dataset):
    missing_values = []
    for i, row in enumerate(dataset):
        for j, value in enumerate(row):
            if value is None:  # Check if the value is missing (None)
                missing_values.append((i, j))  # Record the position of the missing value
    return missing_values

# Test
dataset = [
    [1, 2, 3],
    [4, None, 6],
    [7, 8, 9]
]
print(find_missing_values(dataset))  # Output: [(1, 1)]
