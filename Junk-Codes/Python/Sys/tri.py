import sys

sys.setrecursionlimit(100000)
N = int(input())
memo = [-1] * (N + 1)


def tri(N):
    if N == 0 or N == 1:  # ベースケース1
        if memo[N] == -1:  # 記録がないかチェック
            memo[N] = 0
        return 0
    elif N == 2:  # ベースケース2
        if memo[N] == -1:  # 記録がないかチェック
            memo[N] = 1
        return 1
    else:
        if memo[N] == -1:  # 記録がないかチェック
            memo[N] = tri(N - 1) + tri(N - 2) + tri(N - 3)
        return memo[N]  # 記録された部分を返す


print(tri(N))
