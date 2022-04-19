import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, r, q = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(n)]
num = [1 for _ in range(n)]


def foo(x):

    cnt = 1
    for v in graph[x]:
        if not visited[v]:
            visited[v] = True
            foo(v)
            cnt += num[v]

    num[x] = cnt


visited[r - 1] = True
foo(r - 1)

for _ in range(q):
    a = int(input())

    sys.stdout.write(str(num[a - 1]) + '\n')
