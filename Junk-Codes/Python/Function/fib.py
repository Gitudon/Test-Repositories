N = int(input())
memo = [-1] * (N + 1)


def fib(N):
    if N == 0 or N == 1:
        if memo[N] == -1:
            memo[N] = 1
        return memo[N]
    else:
        if memo[N] == -1:
            memo[N] = fib(N - 1) + fib(N - 2)
        return memo[N]


fib(N)
print(memo[N])
