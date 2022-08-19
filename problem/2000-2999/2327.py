import sys
input = sys.stdin.readline

h, n = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(n)]
li.sort(key=lambda x: -x[1])

dp = [-1 for _ in range(h + 1)]
dp[0] = float('inf')

for he, ve in li:
    for i in range(h, he - 1, -1):
        if dp[i - he] != -1:
            dp[i] = max(dp[i], min(dp[i - he], ve))

    if dp[h] != -1:
        break

print(dp[h])
