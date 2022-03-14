import heapq
import sys
input = sys.stdin.readline

n, e = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

a, b = map(int, input().split())

def dijkstra(start):
    minDis = [sys.maxsize] * (n + 1)
    minDis[start] = 0

    hq = [(start, 0)]

    while hq:
        curPos, curDis = heapq.heappop(hq)

        for newPos, w in graph[curPos]:
            newDis = curDis + w
            if minDis[newPos] > newDis:
                minDis[newPos] = newDis
                heapq.heappush(hq, (newPos, newDis))

    return minDis

one = dijkstra(1)
A = dijkstra(a)
B = dijkstra(b)

result = min( one[a] + B[n], one[b] + A[n] ) + A[b]
if result > 200000000:
    print(-1)
else:
    print(result)