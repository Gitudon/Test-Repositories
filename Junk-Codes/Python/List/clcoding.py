clcoding = [1, 2, 3, 4]
total = 0
for x in clcoding:
    total += x
    clcoding[0] = total
print(clcoding)
