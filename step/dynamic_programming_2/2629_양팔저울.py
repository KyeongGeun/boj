import sys
input = sys.stdin.readline

n = int(input()) # <= 30
weight = list(map(int, input().split())) # <= 500

m = int(input()) # <= 7
marble = list(map(int, input().split())) # <= 40000
maxi = 15001

dp = [[0 for _ in range(40001)] for _ in range(n)]

dp[0][weight[0]] = 1

for i in range(1, n):
    for j in range(maxi):
        if j == weight[i] or dp[i-1][j]:
            dp[i][j] = 1
        elif j - weight[i] >= 0 and dp[i - 1][j - weight[i]]:
            dp[i][j] = 1
        elif j + weight[i] < maxi and dp[i - 1][j + weight[i]]:
            dp[i][j] = 1
        elif -j + weight[i] >= 0 and dp[i - 1][-j + weight[i]]:
            dp[i][j] = 1

ans = []

for v in marble:
    if dp[-1][v]:
        ans.append('Y')
    else:
        ans.append('N')

print(*ans)
