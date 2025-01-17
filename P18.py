# Simple linear regression without using inbuilt libraries
def simple_linear_regression(x, y):
    n = len(x)
    x_mean = sum(x) / n
    y_mean = sum(y) / n
    
    # Calculating the slope (m)
    numerator = sum([(x[i] - x_mean) * (y[i] - y_mean) for i in range(n)])
    denominator = sum([(x[i] - x_mean) ** 2 for i in range(n)])
    m = numerator / denominator
    
    # Calculating the intercept (b)
    b = y_mean - m * x_mean
    
    return m, b

# Test
x = [1, 2, 3, 4, 5]
y = [3, 4, 2, 4, 5]
m, b = simple_linear_regression(x, y)
print(f"Slope: {m}, Intercept: {b}")
