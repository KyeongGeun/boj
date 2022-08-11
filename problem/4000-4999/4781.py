import sys
input = sys.stdin.readline

ans = []
while True:
    n, m = input().split()

    if n == '0':
        break

    n = int(n)
    m = int(float(m) * 100)

    dp = [0] * (m + 1)

    for _ in range(n):
        c, p = input().split()
        c = int(c)
        p = int(float(p) * 100 + 0.5)
        for i in range(p, m + 1):
            dp[i] = max(dp[i], dp[i - p] + c)

    ans.append(dp[m])

print(*ans, sep='\n')
