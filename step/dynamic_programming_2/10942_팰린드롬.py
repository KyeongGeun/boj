import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

m = int(input())
question = [list(map(int, input().split())) for _ in range(m)]

dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if num[i] == num[i+1]:
        dp[i][i+1] = 1

for l in range(2, n):
    for i in range(n-l):
        if dp[i+1][i+l-1]:
            if num[i] == num[i+l]:
                dp[i][i+l] = 1

for s, e in question:
    print(dp[s-1][e-1])