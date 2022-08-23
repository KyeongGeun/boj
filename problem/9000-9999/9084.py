import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))

    m = int(input())
    dp = [0] * (m + 1)
    dp[0] = 1

    for v in li:
        for i in range(v, m + 1):
            dp[i] += dp[i - v]

    ans.append(dp[m])

print(*ans, sep='\n')
