x = [1, 2, 3]
y = x
y[0] = 10
print(x)  # Output: [10, 2, 3]
z = y.copy()
z[1] = 20
print(y)  # Output: [10, 2, 3]
