import sys
input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]


def func(N, i, bit, start):
    if N >= n - 1:
        return w[i][start] if w[i][start] != 0 else float('inf')

    mini = float('inf')

    if memo[i][bit] != -1:
        return memo[i][bit]

    for j in range(n):
        if w[i][j] != 0 and not bit & (1 << j):
            mini = min(mini, w[i][j] + func(N + 1, j, bit | (1 << j), start))

    memo[i][bit] = mini
    return mini


memo = [[-1 for _ in range(1 << n)] for _ in range(n)]

print(func(0, 0, 1, 0))
