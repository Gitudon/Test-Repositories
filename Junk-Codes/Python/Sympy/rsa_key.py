from find_prime import sieve_of_eratosthenes
import random


def main():
    n = int(input("Size: "))
    prime = sieve_of_eratosthenes(n)
    p = random.choice(prime)
    while True:
        q = random.choice(prime)
        if q != p:
            break
    N = p * q
    fai = (p - 1) * (q - 1)
    e = 65537
    d = pow(e, -1, fai)
    print(f"p: {p}")
    print(f"q: {q}")
    print(f"N: {N}")
    print(f"e: {e}")
    print(f"d: {d}")
    return


if __name__ == "__main__":
    main()
