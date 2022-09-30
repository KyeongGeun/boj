import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

n, m = len(s1), len(s2)

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

mmax = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            mmax = max(mmax, dp[i][j])

print(mmax)
