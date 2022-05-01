import sys
input = sys.stdin.readline

n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]
memo = [[[-1 for _ in range(1 << 3)]
         for _ in range(1 << 3)] for _ in range(n)]


def func(N, bit, start):

    if N >= n - 1:
        if N == n - 1:
            bit |= start
        else:
            return 0

    if memo[N][bit][start] != -1:
        return memo[N][bit][start]

    mini = float('inf')
    for i in range(3):
        if not bit & (1 << i):
            mini = min(mini, li[N][i] + func(N + 1, 1 << i, start))

    memo[N][bit][start] = mini
    return mini


print(min(li[0][0] + func(1, 1, 1), li[0][1] + func(1, 1 <<
      1, 1 << 1), li[0][2] + func(1, 1 << 2, 1 << 2)))
