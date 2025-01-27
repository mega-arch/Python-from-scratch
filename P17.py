# Calculate mean, median, and mode of a dataset
def calculate_statistics(data):
    # Mean
    mean = sum(data) / len(data)
    
    # Median
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]
    
    # Mode
    frequency = {}
    for num in data:
        frequency[num] = frequency.get(num, 0) + 1
    mode = max(frequency, key=frequency.get)
    
    return mean, median, mode

# Test
data = [1, 2, 2, 3, 4, 5, 5, 5, 6]
mean, median, mode = calculate_statistics(data)
print(f"Mean: {mean}, Median: {median}, Mode: {mode}")
