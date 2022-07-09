from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

degree = [0] * n
time = [0] * n
graph = [[] for _ in range(n)]
parent = [[] for _ in range(n)]

for i in range(n):
    li = list(map(int, input().split()))

    degree[i] += len(li) - 2
    time[i] = li[0]

    for j in range(1, len(li) - 1):
        graph[li[j] - 1].append(i)
        parent[i].append(li[j] - 1)

dq = deque()
for i in range(n):
    if degree[i] == 0:
        dq.append(i)

ans = [0] * n
cur = 0
while dq:
    x = dq.pop()

    _max = 0
    for v in parent[x]:
        _max = max(_max, ans[v])

    ans[x] = _max + time[x]

    for v in graph[x]:
        degree[v] -= 1

        if degree[v] == 0:
            dq.append(v)

print(*ans, sep='\n')
