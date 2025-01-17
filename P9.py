# Count the number of digits in a number
def count_digits(num):
    count = 0
    while num > 0:
        num //= 10  # Remove the last digit
        count += 1
    return count

# Test
print(count_digits(12345))  # Output: 5
