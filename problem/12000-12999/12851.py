from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

l = max(n, k) + 2

dp = [-1] * l
cnt = [0] * l

dp[n] = 0
cnt[n] = 1

dq = deque([n])

while dq:
    for _ in range(len(dq)):
        x = dq.popleft()

        nx = (x - 1, x + 1, x << 1)

        for v in nx:
            if v < 0 or v > l - 1:
                continue

            if dp[v] != -1:
                if dp[v] == dp[x] + 1:
                    cnt[v] += cnt[x]
                continue

            cnt[v] += cnt[x]

            dp[v] = dp[x] + 1

            dq.append(v)

    if dp[k] != -1:
        break

print(dp[k], cnt[k], sep='\n')
