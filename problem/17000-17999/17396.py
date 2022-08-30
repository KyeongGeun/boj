from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ward = list(map(int, input().split()))
ward[n - 1] = 0
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))
    graph[b].append((a, c))

hq = [(0, 0)]
INF = float('inf')
memo = [INF] * n
while hq:
    t, x = heappop(hq)

    if memo[x] < t:
        continue

    for v, c in graph[x]:
        if ward[v]:
            continue

        newT = t + c

        if memo[v] > newT:
            memo[v] = newT
            heappush(hq, (newT, v))

print(-1 if memo[n - 1] == INF else memo[n - 1])
