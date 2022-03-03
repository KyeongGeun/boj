from collections import deque
import sys
input = sys.stdin.readline

def dfs(v):
    log.add(v)
    print(v, end=' ')
    for value in graph[v]:
        if value not in log:
            dfs(value)

def bfs(v):
    log.add(v)
    
    q = deque([v])

    while q:
        value = q.popleft()
        print(value, end=' ')
        for v in graph[value]:
            if v not in log:
                q.append(v)
                log.add(v)

    return

n, m, v = map(int, input().split())
graph = [0] + [[] for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, len(graph)):
    graph[i].sort()

log = set()
dfs(v)
print()
log = set()
bfs(v)