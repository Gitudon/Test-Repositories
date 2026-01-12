a = int(input("判定したい自然数を入力　"))
b = 0
c = 0
while c <= a:
    if c == 0:
        b = 0
        c = c + 1
    else:
        d = a % c
        if d == 0:
            b = b + 1
            c = c + 1
        else:
            b = b
            c = c + 1
if b > 2 or a == 1:
    print("入力した自然数は素数ではありません")
else:
    print("入力した自然数は素数です")
