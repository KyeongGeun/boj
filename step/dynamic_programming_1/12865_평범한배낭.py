import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = [0]*(n+1)

dp = [0 for _ in range(m+1)]

for _ in range(1, n+1):
  w, v = map(int, input().split())
  for j in range(m, 0, -1):
    if j >= w:
      dp[j] = max(dp[j-w] + v, dp[j])

print(dp[m])
