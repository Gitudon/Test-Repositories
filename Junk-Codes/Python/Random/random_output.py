import random

a = 0
b = 0
c = list()
d = list()
while a < 1:
    e = input("リストの名前を入力 ")
    f = int(input(e + "に追加する要素の数を整数で入力 "))
    for g in range(f):
        h = input(e + "に追加する要素を入力 ")
        c.append(h)
    print(c)
    i = int(input(e + "から取り出す要素の数を整数で入力 "))
    while b < 1:
        for j in range(i):
            k = random.choice(c)
            print(k)
            c.remove(k)
            d.append(k)
        l = int(input("再試行は1を入力 しないなら2を入力 "))
        if l == 1:
            c.extend(d)
            d.clear()
        else:
            b = 1
    m = int(input("最初からやり直す場合は3を入力 しないなら4を入力 "))
    if m == 3:
        b = 0
        c.clear()
        d.clear()
    else:
        a = 1
