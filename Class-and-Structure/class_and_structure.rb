class Person
  def initialize(name, age)
    @name = name
    @age = age
  end
  def print_profile()
    puts "Name: #{@name}"
    puts "Age: #{@age}"
  end
  def add_age()
    @age += 1
  end
end

class Product < Struct.new(:name, :price, :comments)
end

  def main
  person = Person.new("Mr. Qiita", 15)
  person.print_profile
  product = Product.new("Product A", 1000, ["Good", "About IT"])
  puts product.price * 5
end

main()