from heapq import heappush, heappop
import sys
input = sys.stdin.readline

line = [tuple(map(int, input().split())) for _ in range(int(input()))]

line.sort()

ans = 1
hq = []
for a, b in line:
    while hq and hq[0] <= a:
        heappop(hq)
    heappush(hq, b)
    ans = max(ans, len(hq))

print(ans)
