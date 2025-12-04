a = [1, 2, 3]
b = [10, 20, 30]
for i, j in zip(a, b):
    i += 100
    print(j)

for i, j in zip(a, b):
    print(i, j)
