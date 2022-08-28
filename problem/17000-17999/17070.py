import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1

for i in range(2, n):
    if li[0][i]:
        break
    dp[0][i][0] = 1

for i in range(1, n):
    for j in range(1, n):
        if li[i][j] == 1:
            continue
        dp[i][j][2] += dp[i - 1][j][1] + dp[i - 1][j][2]
        dp[i][j][0] += dp[i][j - 1][0] + dp[i][j - 1][1]

        if li[i - 1][j] or li[i][j - 1]:
            continue
        dp[i][j][1] += sum(dp[i - 1][j - 1])

print(sum(dp[n - 1][n - 1]))
