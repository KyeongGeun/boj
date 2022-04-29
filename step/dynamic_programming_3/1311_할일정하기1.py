import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
memo = [[-1 for _ in range(2 ** n)] for _ in range(n)]


def dp(N, bit):
    if N >= n:
        return 0

    if memo[N][bit] != -1:
        return memo[N][bit]

    mini = float('inf')
    for i in range(n):
        if not bit & (1 << i):
            mini = min(mini, li[N][i] + dp(N + 1, bit | (1 << i)))

    memo[N][bit] = mini
    return mini


print(dp(0, 0))
