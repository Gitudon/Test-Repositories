import time
from sympy import isprime
import math


def simple(n):
    prime = []
    for i in range(2, n + 1):
        flag = False
        for j in range(2, i):
            if i % j == 0:
                flag = True
                break
        if not flag:
            prime.append(i)
    return prime


def root(n):
    prime = []
    for i in range(2, n + 1):
        flag = False
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                flag = True
                break
        if not flag:
            prime.append(i)
    return prime


def module(n):
    prime = []
    for i in range(n + 1):
        if isprime(i):
            prime.append(i)
    return prime


def sieve_of_eratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    Prime = []
    for p in range(2, n + 1):
        if prime[p]:
            Prime.append(p)
    return Prime


def main():
    flag = int(input("1, 2, 3, 4, 5: "))
    n = int(input("size: "))
    start_time = time.time()
    if flag == 1:
        prime = simple(n)
    elif flag == 2:
        prime = root(n)
    elif flag == 3:
        prime = module(n)
    elif flag == 4:
        prime = sieve_of_eratosthenes(n)
    else:
        if isprime(n):
            print("Prime.")
            exit()
    for p in prime:
        print(p)
    end_time = time.time()
    print("time: " + str(end_time - start_time))


if __name__ == "__main__":
    main()

# 高速化アイディア：末尾が5なら弾く
