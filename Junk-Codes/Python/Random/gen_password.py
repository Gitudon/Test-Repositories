import random

a = int(input("桁数入力 >"))
b = ""
for i in range(a):
    c = random.randint(0, 9)
    b += str(c)
print("Your password is: " + b)
