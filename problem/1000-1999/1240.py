import heapq
import sys
input = sys.stdin.readline


def bfs(N, K):
    hq = [(0, N)]
    visited[N] = True
    while hq:
        c, x = heapq.heappop(hq)

        for v, c2 in graph[x]:

            if v == K:
                return c + c2

            if visited[v]:
                continue
            visited[v] = True

            heapq.heappush(hq, (c + c2, v))


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c, = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for _ in range(m):
    visited = [False] * (n + 1)
    a, b = map(int, input().split())
    print(bfs(a, b))
