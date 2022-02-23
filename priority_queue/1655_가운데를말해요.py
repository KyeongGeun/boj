import heapq
import sys
input = sys.stdin.readline

ans = []
left_hq = []
right_hq = []

n = int(input())

num = int(input())
left_hq.append(-num)
ans.append(num)

for _ in range(n-1):
    num = int(input())
    if num > -left_hq[0]:
        heapq.heappush(right_hq, num)
        if len(left_hq) < len(right_hq):
            heapq.heappush(left_hq, -(heapq.heappop(right_hq)))
    else:
        heapq.heappush(left_hq, -num)
        if len(left_hq) > len(right_hq) + 1:
            heapq.heappush(right_hq, -(heapq.heappop(left_hq)))

    print(left_hq)
    print(right_hq)
    ans.append(-left_hq[0])

print(*ans, sep='\n')