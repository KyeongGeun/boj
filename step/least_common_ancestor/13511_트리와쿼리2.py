from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dq = deque()
dq.append(1)
visited = [False] * (n + 1)
parent = [[0 for _ in range(n + 1)] for _ in range(17)]
d = [[0 for _ in range(n + 1)] for _ in range(17)]
degree = [0] * (n + 1)

while dq:
    x = dq.popleft()
    visited[x] = True
    
    for v, c in graph[x]:
        if not visited[v]:
            parent[0][v] = x
            d[0][v] = c
            dq.append(v)
            degree[v] = degree[x] + 1

for i in range(1, 17):
    for j in range(1, n + 1):
        parent[i][j] = parent[i - 1][parent[i - 1][j]]
        d[i][j] = d[i - 1][j] + d[i - 1][parent[i - 1][j]]

for _ in range(int(input())):
    li = list(map(int, input().split()))

    u, v = li[1], li[2]
    if li[0] == 1:
        if degree[u] < degree[v]:
            u, v = v, u
        
        gap = degree[u] - degree[v]

        cnt = 0
        for i in range(17):
            if gap & (1 << i):
                cnt += d[i][u]
                u = parent[i][u]

        for i in range(16, -1, -1):
            if parent[i][u] != parent[i][v]:
                cnt += d[i][u] + d[i][v]
                u = parent[i][u]
                v = parent[i][v]
        
        if u != v:
            for i in range(17):
                if parent[i][u] == parent[i][v]:
                    cnt += d[i][u] + d[i][v]
                    break
        
        print(cnt)
    
    else:
        k = li[3]
        gap = abs(degree[u] - degree[v])

        cntu = 0
        cntv = 0
        x, y = u, v
        if degree[u] > degree[v]:
            for i in range(17):
                if gap & (1 << i):
                    x = parent[i][x]
                    cntu += 2 ** i
        else:
            for i in range(17):
                if gap & (1 << i):
                    y = parent[i][y]
                    cntv += 2 ** i

        for i in range(16, -1, -1):
            if parent[i][x] != parent[i][y]:
                cntu += 2 ** i
                cntv += 2 ** i
                x = parent[i][x]
                y = parent[i][y]

        if x != y:
            for i in range(17):
                if parent[i][x] == parent[i][y]:
                    cntu += 2 ** i
                    cntv += 2 ** i
                    x = parent[i][x]
                    break
        
        k -= 1
        if cntu >= k:
            ans = u
        else:
            k -= cntu
            k = cntv - k
            ans = v

        for i in range(17):
            if k & (1 << i):
                ans = parent[i][ans]

        print(ans)
