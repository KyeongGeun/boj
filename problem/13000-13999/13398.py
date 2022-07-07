import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

dp = [0] * (n)
dp2 = [0] * (n)
dp[0] = li[0]
dp2[0] = li[0]
for i in range(1, n):
    dp[i] = max(dp[i - 1] + li[i], li[i])
    dp2[i] = max(dp[i - 1], dp2[i - 1] + li[i], li[i])

print(max(max(dp), max(dp2)))
