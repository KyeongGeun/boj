import sys
input = sys.stdin.readline
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(1, n):
    dp[i-1][i] = li[i-1][0] * li[i-1][1] * li[i][1]

for j in range(2, n):
    for i in range(j-2, -1, -1):
        mini = sys.maxsize
        for k in range(j-i):
            mini = min(mini, dp[i][i+k] + dp[i+k+1][j] + li[i][0] * li[i+k][1] * li[j][1])
        dp[i][j] = mini

print(dp[0][n-1])
