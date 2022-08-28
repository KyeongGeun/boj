import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1

for i in range(n):
    for j in range(n):
        if li[i][j] == 1:
            continue
        if i != 0:
            dp[i][j][2] += dp[i - 1][j][1] + dp[i - 1][j][2]
        if j != 0:
            dp[i][j][0] += dp[i][j - 1][0] + dp[i][j - 1][1]

        if i == 0 or j == 0 or li[i - 1][j] == 1 or li[i][j - 1] == 1:
            continue
        dp[i][j][1] += sum(dp[i - 1][j - 1])

print(sum(dp[n - 1][n - 1]))
