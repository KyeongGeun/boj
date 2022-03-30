from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [-1] * (max(n, k) + 3)
dp[n] = 0
pre = [-1] * (max(n, k) + 3)

dq = deque([n])
dx = [0, -1, 1]

cnt = 0
while dq:
    cnt += 1
    for _ in range(len(dq)):
        x = dq.popleft()
        dx[0] = x

        for i in range(3):
            a = x + dx[i]

            if 0 <= a <= max(n, k) + 2:
                if dp[a] == -1:
                    dp[a] = cnt
                    pre[a] = x
                    dq.append(a)

print(dp[k])

answer = []
i = k
for _ in range(dp[k] + 1):
    answer.append(i)
    i = pre[i]

print(*answer[::-1])