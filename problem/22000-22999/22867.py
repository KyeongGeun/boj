# 파싱 필요 X
# heapq 필요 X

import heapq
import sys
input = sys.stdin.readline

n = int(input())

li = []

for i in range(n):
    a, b = input().split()

    s = int(a[:2]) * 3600 + int(a[3:5]) * 60 + float(a[6:])
    e = int(b[:2]) * 3600 + int(b[3:5]) * 60 + float(b[6:])
    s = int(s * 1000)
    e = int(e * 1000)

    li.append((s, e))

li.sort()

_max = 0
hq = []
for i in range(n):
    while hq and hq[0] <= li[i][0]:
        heapq.heappop(hq)

    heapq.heappush(hq, li[i][1])
    _max = max(_max, len(hq))

print(_max)
