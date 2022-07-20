import math
import sys
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

parent = [[-1 for _ in range(n + 1)] for _ in range(int(math.log(n, 2)) + 1)]
weight = [[0 for _ in range(n + 1)] for _ in range(len(parent))]
depth = [0] * (n + 1)
visited = [False] * (n + 1)
visited[1] = True
parent[0][1] = 1

stack = [1]
while stack:
    x = stack.pop()

    for v, w in graph[x]:
        if visited[v]:
            continue
        visited[v] = True

        depth[v] = depth[x] + 1
        parent[0][v] = x
        weight[0][v] = w
        stack.append(v)

for i in range(1, len(parent)):
    for j in range(1, n + 1):
        parent[i][j] = parent[i - 1][parent[i - 1][j]]
        weight[i][j] = weight[i - 1][parent[i - 1][j]] + weight[i - 1][j]

ans = []
for _ in range(int(input())):
    a, b = map(int, input().split())

    if depth[a] < depth[b]:
        a, b = b, a

    d = depth[a] - depth[b]

    cnt = 0
    for i in range(len(parent)):
        if d & (1 << i):
            cnt += weight[i][a]
            a = parent[i][a]

    for i in range(len(parent) - 1, -1, -1):
        if parent[i][a] == 0 or parent[i][a] == parent[i][b]:
            continue
        cnt += weight[i][a]
        cnt += weight[i][b]
        a = parent[i][a]
        b = parent[i][b]

    if a != b:
        for i in range(len(parent)):
            if parent[i][a] == parent[i][b]:
                cnt += weight[i][a]
                cnt += weight[i][b]
                a = parent[i][a]
                b = parent[i][b]
                break

    ans.append(cnt)

print(*ans, sep='\n')
