import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

if li[0][0] == 0:
    dp[0][0] = 1

for i in range(1, n):
    dp[i][0] = dp[i - 1][0]
    if (dp[i - 1][0] % 3) == li[i][0]:
        dp[i][0] += 1

    dp[0][i] = dp[0][i - 1]
    if (dp[0][i - 1] % 3) == li[0][i]:
        dp[0][i] += 1

for i in range(1, n):
    for j in range(1, n):
        if (dp[i - 1][j] % 3) == li[i][j]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + 1)
        else:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

        if (dp[i][j - 1] % 3) == li[i][j]:
            dp[i][j] = max(dp[i][j], dp[i][j - 1] + 1)
        else:
            dp[i][j] = max(dp[i][j], dp[i][j - 1])

print(dp[-1][-1])
