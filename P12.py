# Print an inverted triangle pattern
def inverted_triangle(n):
    for i in range(n, 0, -1):
        print("*" * i)

# Test
inverted_triangle(5)
# Output:
# *****
# ****
# ***
# **
# *
