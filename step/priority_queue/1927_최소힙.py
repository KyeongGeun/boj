import heapq
import sys
input = sys.stdin.readline

hq = []
ans = []

for _ in range(int(input())):
    num = int(input())
    if num == 0:
        if hq:
            ans.append(hq[0])
            heapq.heappop(hq)
        else:
            ans.append(0)
    else:
        heapq.heappush(hq, num)

print(*ans, sep='\n')