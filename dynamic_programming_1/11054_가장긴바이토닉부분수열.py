import sys
input = sys.stdin.readline

n = int(input())
li = [*map(int, input().split())]

dp1 = [1]*n
dp2 = [1]*n

for i in range(n):
  for j in range(i):
    if li[j] < li[i]:
      dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(-1, -n-1, -1):
  for j in range(-1, i, -1):
    if li[j] < li[i]:
      dp2[-i-1] = max(dp2[-i-1], dp2[-j-1] + 1)

m = 1

for i in range(n):
  temp = dp1[i]
  for j in range(1, n-i-1):
      if li[i] != li[i+j]:
        m = max(m, temp + dp2[n-i-1-j])

print(m)
