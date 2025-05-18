#include <iostream>
#include <string>
using namespace std;

class Person
{
public:
    string name;
    int age;
    void print_profile()
    {
        cout << "Name: " << name << "\nAge: " << age << endl;
    }
    void add_age()
    {
        age++;
    }
};

typedef struct productinfo
{
    string name;
    int price;
    string comments[50];
} productinfo;

int main(void)
{
    Person person;
    person.name = "Mr. Qiita";
    person.age = 15;
    person.print_profile();
    productinfo product;
    product.name = "Product A";
    product.price = 1000;
    product.comments[0] = "Good";
    product.comments[1] = "About IT";
    cout << product.price * 5 << endl;
    return 0;
}