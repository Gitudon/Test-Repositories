class Book:
    def set__price(self, val):
        self.__price = val + 1

    def get__price(self):
        return self.__price + 1


obj = Book()
obj.set__price(100)
print(obj.get__price())
