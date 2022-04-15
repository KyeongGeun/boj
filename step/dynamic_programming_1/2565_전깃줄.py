import sys
input = sys.stdin.readline

n = int(input())
li = []

for i in range(n):
  x, y = map(int, input().split())
  li.append([x, y])

li.sort()

for i in range(n):
  li[i] = li[i][1]

dp = [1]*n

for i in range(n):
  for j in range(i):
    if li[i] > li[j]:
      dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))
