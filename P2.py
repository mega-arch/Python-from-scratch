# Reverse a string without using inbuilt reverse function
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Adding each character to the front
    return reversed_str

# Test
print(reverse_string("hello"))  # Output: "olleh"
