import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(N, d):
    depth[N] = d
    for v in graph[N]:
        dfs(v, d + 1)


for _ in range(int(input())):
    n = int(input())

    graph = [[] for _ in range(n + 1)]
    parent = [-1] * (n + 1)
    depth = [0] * (n + 1)

    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        parent[b] = a

    for i in range(1, n + 1):
        if parent[i] == -1:
            dfs(i, 0)
            break

    a, b = map(int, input().split())

    while depth[a] > depth[b]:
        a = parent[a]

    while depth[b] > depth[a]:
        b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]

    print(a)
