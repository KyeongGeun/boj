from collections import deque
import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    n, k = map(int, input().split())

    li = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    parent = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    bool = [False] * (n + 1)

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        parent[b].append(a)
        degree[b] += 1

    w = int(input())

    dq = deque([w])
    bool[w] = True

    while dq:
        x = dq.popleft()

        for v in parent[x]:
            if bool[v]:
                continue
            bool[v] = True
            dq.append(v)

    dp = [-float('inf')] * (n + 1)
    for i in range(1, n + 1):
        if bool[i] and degree[i] == 0:
            dq.append(i)
            dp[i] = li[i]

    while dq:
        x = dq.popleft()

        for v in parent[x]:
            if bool[v]:
                dp[x] = max(dp[x], dp[v] + li[x])

        if x == w:
            break

        for v in graph[x]:
            degree[v] -= 1

            if degree[v] == 0 and bool[v]:
                dq.append(v)

    ans.append(dp[w])

print(*ans, sep='\n')
