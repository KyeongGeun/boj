from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

dq = deque()

for i in range(1, n + 1):
    if degree[i] == 0:
        dq.append(i)

ans = [0] * (n + 1)
cnt = 0
while dq:
    cnt += 1
    for _ in range(len(dq)):
        x = dq.popleft()
        ans[x] = cnt

        for v in graph[x]:
            degree[v] -= 1

            if degree[v] == 0:
                dq.append(v)

print(*ans[1:])
