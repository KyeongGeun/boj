import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [0 for _ in range(k+1)]
dp[0] = 1


for v in coins:
    for i in range(1, k+1):
        if i - v >= 0:
            dp[i] += dp[i - v]


print(dp[-1])
