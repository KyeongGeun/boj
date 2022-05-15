from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
parent = [[(0, float('inf'), -float('inf'))
           for i in range(n + 1)] for _ in range(17)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


dq = deque()
dq.append(1)
depth = 0
visited = [False] * (n + 1)
while dq:
    for _ in range(len(dq)):
        x = dq.popleft()
        degree[x] = depth
        visited[x] = True

        for v, d in graph[x]:
            if not visited[v]:
                parent[0][v] = (x, d, d)
                dq.append(v)
    depth += 1

for i in range(1, 17):
    for j in range(1, n + 1):
        if parent[i - 1][parent[i - 1][j][0]][0] == 0:
            continue
        parent[i][j] = (parent[i - 1][parent[i - 1][j][0]][0],
                        min(parent[i - 1][j][1], parent[i - 1]
                            [parent[i - 1][j][0]][1]),
                        max(parent[i - 1][j][2], parent[i - 1]
                            [parent[i - 1][j][0]][2]))

for _ in range(int(input())):
    x, y = map(int, input().split())

    if degree[y] > degree[x]:
        x, y = y, x

    d = degree[x] - degree[y]

    mmin = float('inf')
    mmax = -float('inf')
    for i in range(17):
        if d & (1 << i):
            mmin = min(mmin, parent[i][x][1])
            mmax = max(mmax, parent[i][x][2])
            x = parent[i][x][0]

    for i in range(16, -1, -1):
        if parent[i][x][0] != parent[i][y][0]:
            mmin = min(mmin, parent[i][x][1], parent[i][y][1])
            mmax = max(mmax, parent[i][x][2], parent[i][y][2])
            x = parent[i][x][0]
            y = parent[i][y][0]

    if x != y:
        for i in range(17):
            if parent[i][x][0] == parent[i][y][0]:
                mmin = min(mmin, parent[i][x][1], parent[i][y][1])
                mmax = max(mmax, parent[i][x][2], parent[i][y][2])
                break

    print(mmin, mmax)
