class Person:
    def __init__(self):
        self.name = ""
        self.age = 0
    def print_profile(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    def add_age(self):
        self.age += 1

class ProductInfo:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.comments = [""]

def main():
    person = Person()
    person.name = "Mr. Qiita"
    person.age = 15
    person.print_profile()
    product = ProductInfo()
    product.name = "Product A"
    product.price = 1000
    product.comments = ["Good", "About IT"]
    print(product.price * 5)

if __name__=="__main__":
    main()