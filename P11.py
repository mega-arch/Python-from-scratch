# Calculate the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiply result by each number from 1 to n
    return result

# Test
print(factorial(5))  # Output: 120
