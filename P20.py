# Normalize data using min-max normalization
def normalize_data(data):
    min_value = min(data)
    max_value = max(data)
    return [(x - min_value) / (max_value - min_value) for x in data]

# Test
data = [10, 20, 30, 40, 50]
normalized_data = normalize_data(data)
print(normalized_data)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
