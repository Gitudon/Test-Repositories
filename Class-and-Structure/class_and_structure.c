#include <stdio.h>

typedef struct person
{
    char name[50];
    int age;
} Person;

void print_profile(const Person *p)
{
    printf("Name: %s\n", p->name);
    printf("Age: %d\n", p->age);
}

void add_age(Person *p)
{
    p->age++;
}

typedef struct productinfo
{
    char name[50];
    int price;
    char comments[50][100];
} ProductInfo;

int main(void)
{
    Person qiita = {"Mr. Qiita", 15};
    Person *p = &qiita;
    print_profile(p);
    ProductInfo product = {"Product A", 1000, {"Good", "About IT"}};
    printf("%d\n", product.price * 5);
    return 0;
}
