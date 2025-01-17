# Scatter plot from scratch using ASCII art (for fun and simplicity)
def scatter_plot(x, y):
    max_x = max(x)
    max_y = max(y)
    
    for y_val in range(max_y, -1, -1):
        line = ""
        for x_val in range(max_x + 1):
            if (x_val, y_val) in zip(x, y):
                line += "*"
            else:
                line += " "
        print(line)

# Test
x = [1, 2, 3, 4, 5]
y = [3, 2, 4, 5, 1]
scatter_plot(x, y)
