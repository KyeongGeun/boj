import heapq
import sys
input = sys.stdin.readline

n = int(input())

li = []
for _ in range(n):
    a, b = map(int, input().split())

    if a > b:
        a, b = b, a

    li.append((a, b))

l = int(input())

li.sort(key=lambda x: (x[1], -x[0]), reverse=True)

hq = []
ans = 0
while li:
    x, y = li.pop()

    if y - x > l:
        continue

    heapq.heappush(hq, x)

    while hq and hq[0] < y - l:
        heapq.heappop(hq)

    ans = max(ans, len(hq))

print(ans)
