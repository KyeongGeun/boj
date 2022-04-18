from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

graph = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b)
    graph[b].append(a)


def dp(x, b):

    ssum1 = 0
    ssum2 = 0
    if memo[x][b] == -1:
        for v in graph[x]:
            if not visited[v]:
                visited[v] = True
                ssum1 += dp(v, 0)
                ssum2 += dp(v, 1)
        memo[x][0] = ssum2
        memo[x][1] = max(li[x] + ssum1, ssum2)

    return memo[x][b]


visited = [False] * n
visited[0] = True
memo = [[-1, -1] for _ in range(n)]

print(dp(0, 1))

dq = deque()
ans = []
if memo[0][1] > memo[0][0]:
    dq.append([0, 1])
else:
    dq.append([0, 0])

visited = [False] * n
visited[0] = True

while dq:
    x, b = dq.popleft()

    ssum1 = 0
    ssum2 = 0

    li2 = []

    for v in graph[x]:
        if not visited[v]:
            visited[v] = True
            ssum1 += memo[v][0]
            ssum2 += memo[v][1]
            li2.append(v)

    c = 0
    if b == 1 and memo[x][b] == li[x] + ssum1:
        ans.append(x + 1)
    else:
        c = 1

    for v in li2:
        dq.append([v, c])

print(*sorted(ans))
