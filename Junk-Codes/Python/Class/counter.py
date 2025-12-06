class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 3


Counter.increment()
Counter.increment()
print(Counter.count)
