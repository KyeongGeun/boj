import sys
input = sys.stdin.readline


def dfs(num, cnt):
    if cnt == 4:
        print(1)
        exit(0)
    for v in graph[num]:
        if not visited[v]:
            visited[v] = True
            if dfs(v, cnt + 1):
                return True
            visited[v] = False
    return False


n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n

for i in range(n):
    visited[i] = True
    if dfs(i, 0):
        print(1)
        break
    visited[i] = False
else:
    print(0)
