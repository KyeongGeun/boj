from collections import deque


def bfs(n, a, graph):
    dist = [-1] * (n + 1)
    dist[a] = 0
    dq = deque([a])

    while dq:
        x = dq.popleft()

        for y in graph[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                dq.append(y)

    return dist


def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]

    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    dist = bfs(n, destination, graph)

    return [dist[a] if dist[a] != float('inf') else -1 for a in sources]
