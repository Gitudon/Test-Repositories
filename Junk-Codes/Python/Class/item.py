class Item:
    def __init__(self, p):
        self._p = p

    @property
    def price(self):
        return self._p + 10


i = Item(50)
print(i.price)
