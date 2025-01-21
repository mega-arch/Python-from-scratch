# Check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    c=0
    for i in range(2, num+1): # Loop from 2 since 1 is not a prime and num+1 for inclusive
        if num % i == 0:  # If num is divisible by any number other than 1 and itself
            c+=1
    if c<2:
        return False
    else:
        return True
# Test
print(is_prime(29))  # Output: True
