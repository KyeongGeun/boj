import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # <= 100, <= 10_000_000

mem = list(map(int, input().split())) # <= 10_000_000
cost = list(map(int, input().split())) # <= 100

dp = [0] * (sum(cost)) + 1)

for i in range(n):
    for j in range(len(dp)-1, -1, -1):
        dp[j] = max(dp[j], dp[j - cost[i]] + mem[i])
        if j - 1 < cost[i]:
            break

for i, v in enumerate(dp):
    if v >= m:
        print(i)
        break
