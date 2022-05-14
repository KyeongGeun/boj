import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())

graph = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
sparce = [[0 for _ in range(n + 1)] for _ in range(17)]
visited = [False] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(N, K):
    visited[N] = True
    degree[N] = K
    for v in graph[N]:
        if not visited[v]:
            sparce[0][v] = N
            dfs(v, K + 1)


dfs(1, 0)

for i in range(1, 17):
    for j in range(1, n + 1):
        sparce[i][j] = sparce[i - 1][sparce[i - 1][j]]

for _ in range(int(input())):
    a, b = map(int, input().split())

    if degree[a] < degree[b]:
        a, b = b, a

    d = degree[a] - degree[b]

    x, y = a, b
    for i in range(17):
        if d & (1 << i):
            x = sparce[i][x]

    for i in range(16, -1, -1):
        if sparce[i][x] == 0 or sparce[i][x] == sparce[i][y]:
            continue
        x = sparce[i][x]
        y = sparce[i][y]

    if x != y:
        for i in range(17):
            if sparce[i][x] == sparce[i][y]:
                x = sparce[i][x]
                y = sparce[i][y]
                break

    print(x)
