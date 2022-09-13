from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))

a, b = map(int, input().split())

dist = [float('inf')] * (n + 1)
dist[a] = 0

hq = [(0, a)]

while hq:
    d, x = heappop(hq)

    if dist[x] < d:
        continue

    for y, c in graph[x]:
        new_d = d + c
        if new_d < dist[y]:
            dist[y] = new_d
            heappush(hq, (new_d, y))

print(dist[b])
