# Count the number of vowels in a string
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count

# Test
print(count_vowels("hello world"))  # Output: 3
