class Num:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Num(self.x * other.x)


n1 = Num(3)
n2 = Num(4)
print((n1 + n2).x)
