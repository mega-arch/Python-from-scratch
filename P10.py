# Count the number of vowels in a string
def count_vowels(s):
    vowels = "aeiou" #declaring vowels in seperate variable
    count = 0
    for char in s: #in each iteration checks individual character 
        if char.lower() in vowels:
            count += 1
    return count

print(count_vowels("hello world"))  # Output: 3
