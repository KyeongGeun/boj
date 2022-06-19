import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
hq = list(map(lambda x: -int(x), input().split()))
heapq.heapify(hq)

_min = min(hq)

answer = 0
while hq:
    li = [-heapq.heappop(hq) for _ in range(min(m, len(hq)))]

    answer += li[-1]
    for v in li:
        if v > li[-1]:
            heapq.heappush(hq, -v + li[-1])

print(answer)
