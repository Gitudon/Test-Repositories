import random

A = 0

a = random.randint(0, 9)
b = random.randint(0, 9)
if b == a:
    b = random.randint(0, 9)
c = random.randint(0, 9)
if c == a or c == b:
    c = random.randint(0, 9)

print("数当てゲーム")
print("三桁の重複無しの数字を一桁ずつ入力して正解を目指そう")
print("位置と数字が当たってたらH、数字だけ当たってたらB")

while A < 3:
    d = int(input("一桁目　"))
    e = int(input("二桁目　"))
    f = int(input("三桁目　"))
    if (
        (d == a and e != b and f != c and e != c and f != b)
        or (d != a and e == b and f != c and d != c and f != a)
        or (d != a and e != b and f == c and d != b and e != a)
    ):
        print("1H0B")
    elif (
        (d == a and e == b and f != c)
        or (d == a and e != b and f == c)
        or (d != a and e == b and f == c)
    ):
        print("2H0B")
    elif d == a and e == b and f == c:
        A += 3
    elif (d == b and e != a and e != c and f != a and f != c) or (
        d == c and e != a and e != b and f != a and f != b
    ):
        print("0H1B")
    elif (e == a and d != b and d != c and f != b and f != c) or (
        e == c and d != a and d != b and f != a and f != b
    ):
        print("0H1B")
    elif (f == a and d != b and d != c and e != b and e != c) or (
        f == b and e != a and e != c and d != a and d != c
    ):
        print("0H1B")
    elif (
        (d == b and e == a and f != c)
        or (d == b and e == c and f != a)
        or (d == c and e == a and f != b)
    ):
        print("0H2B")
    elif (
        (f == b and e == a and d != c)
        or (f == b and e == c and d != a)
        or (e == c and f == a and d != b)
    ):
        print("0H2B")
    elif (
        (d == b and e != c and f == a)
        or (d == c and e != b and f == a)
        or (d == c and e != a and f == b)
    ):
        print("0H2B")
    elif (d == b and e == c and f == a) or (d == c and e == a and f == b):
        print("0H3B")
    elif (
        (d == a and e == c and f == b)
        or (d == c and e == b and f == a)
        or (d == b and e == a and f == c)
    ):
        print("1H2B")
    elif (
        (d == a and e == c and f != b)
        or (d != c and e == b and f == a)
        or (d != b and e == a and f == c)
    ):
        print("1H1B")
    elif d == 666 and e == 666 and f == 666:
        print("debug:　" + str(a) + str(b) + str(c))
        A += 3
    else:
        print("0H0B")

print("正解！答えは　" + str(a) + str(b) + str(c))
