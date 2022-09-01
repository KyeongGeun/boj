import sys
input = sys.stdin.readline
INF = float('inf')

n = int(input())
li = [[INF] * (n + 1)]
for _ in range(n):
    li.append([INF] + list(map(int, input().split())))

dp = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
dp[1][1] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 == j:
            continue

        if li[i - 1][j] > li[i][j]:
            a = dp[i - 1][j]
        else:
            a = dp[i - 1][j] + li[i][j] - li[i - 1][j] + 1

        if li[i][j - 1] > li[i][j]:
            b = dp[i][j - 1]
        else:
            b = dp[i][j - 1] + li[i][j] - li[i][j - 1] + 1

        dp[i][j] = min(a, b)

print(dp[n][n])
