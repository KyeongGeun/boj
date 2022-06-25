import sys
input = sys.stdin.readline


def dfs(num, cnt):
    if cnt == 4:
        print(1)
        exit(0)
    for v in graph[num]:
        if not visited[v]:
            visited[v] = True
            dfs(v, cnt + 1)
            visited[v] = False


n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n

for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)
