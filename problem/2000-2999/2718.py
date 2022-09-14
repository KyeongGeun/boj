import sys
input = sys.stdin.readline

dp = [0] * 22
dp[0] = 1
dp[1] = 1

for i in range(2, len(dp)):
    dp[i] = dp[i - 1] + dp[i - 2] * 4
    for j in range(i - 3, -1, -1):
        dp[i] += dp[j] * 2
    for j in range(i - 4, -1, -2):
        dp[i] += dp[j]
ans = []
for _ in range(int(input())):
    ans.append(dp[int(input())])

print(*ans, sep='\n')
