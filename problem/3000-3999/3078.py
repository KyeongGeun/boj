from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

li = [0] * n

for i in range(n):
    li[i] = len(input()) - 1

dqli = [deque() for _ in range(21)]
ans = 0
for i in range(n):
    l = li[i]
    dqli[l].append(i)

    while dqli[l] and i - dqli[l][0] > k:
        dqli[l].popleft()

    ans += len(dqli[l]) - 1

print(ans)
