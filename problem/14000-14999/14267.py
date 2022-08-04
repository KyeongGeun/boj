import sys
input = sys.stdin.readline


def func(x):
    if dp[x] != -1:
        return dp[x]

    dp[x] = func(parent[x]) + li[x]

    return dp[x]


n, m = map(int, input().split())

parent = [-1] + list(map(int, input().split()))

dp = [-1] * (n + 1)
li = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    li[a] += b

dp[1] = 0

for i in range(2, n + 1):
    if dp[i] == -1:
        func(i)

print(*dp[1:])
