import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [float('inf')] * (k + 1)
dp[0] = 0

for _ in range(n):
    v = int(input())
    for i in range(v, k + 1):
        dp[i] = min(dp[i], dp[i - v] + 1)

if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])
