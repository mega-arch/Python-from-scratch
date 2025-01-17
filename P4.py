# Print a right-angle triangle pattern
def triangle_pattern(n):
    for i in range(1, n + 1):
        print("*" * i)

# Test
triangle_pattern(5)
# Output:
# *
# **
# ***
# ****
# *****
