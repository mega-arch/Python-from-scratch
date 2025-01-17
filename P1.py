# Check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num / 2) + 1):  # Loop through possible divisors
        if num % i == 0:  # If num is divisible by any number other than 1 and itself
            return False
    return True

# Test
print(is_prime(29))  # Output: True
