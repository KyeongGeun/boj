import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(x):
    visited[x] = True
    _max = 1
    idx = x
    for v in graph[x]:
        if visited[v]:
            continue

        a, b = dfs(v)
        if _max < a + 1:
            _max = a + 1
            idx = b

    return (_max, idx)


n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
a, b = dfs(1)

visited = [False] * (n + 1)
a, b = dfs(b)

print(a // 2)
