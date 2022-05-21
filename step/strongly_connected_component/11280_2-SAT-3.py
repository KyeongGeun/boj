import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def func(N):
    global cnt
    cnt += 1

    idx[N] = cnt
    visited[N] = True
    stack.append(N)

    ret = cnt
    for v in graph[N]:
        if not visited[v]:
            ret = min(ret, func(v))
        elif not finished[v]:
            ret = min(ret, idx[v])

    if ret == idx[N]:
        li = []
        id = len(scc)
        while stack:
            x = stack.pop()
            idx_in_scc[x] = id
            finished[x] = True
            li.append(x)

            if x == N:
                scc.append(li)
                break

    return ret


n, m = map(int, input().split())

graph = [[] for _ in range(2 * n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[-a].append(b)
    graph[-b].append(a)


visited = [False] * (2 * n + 1)
finished = [False] * (2 * n + 1)
idx = [0] * (2 * n + 1)
idx_in_scc = [0] * (2 * n + 1)
stack = []
scc = []
cnt = 0

for i in range(1, n + 1):
    if not visited[i]:
        func(i)
    if not visited[-i]:
        func(-i)

ans = 1
for i in range(1, n + 1):
    if idx_in_scc[i] == idx_in_scc[-i]:
        ans = 0
        break

print(ans)
