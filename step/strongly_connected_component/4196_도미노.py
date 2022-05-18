import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def func(N):
    global cnt
    cnt += 1
    idx[N] = cnt

    visited[N] = True
    stack.append(N)

    rst = cnt
    for v in graph[N]:
        if not visited[v]:
            rst = min(rst, func(v))
        elif not finished[v]:
            rst = min(rst, idx[v])

    if rst == idx[N]:
        li = []
        id = len(scc)
        while stack:
            x = stack.pop()

            finished[x] = True
            li.append(x)
            idx_in_scc[x] = id

            if x == N:
                scc.append(li)
                break

    return rst


ans = []
for _ in range(int(input())):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    finished = [False] * (n + 1)
    idx = [0] * (n + 1)
    idx_in_scc = [0] * (n + 1)
    stack = []
    scc = []

    cnt = 0

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    for i in range(1, n + 1):
        if not visited[i]:
            func(i)

    len_scc = len(scc)
    degree = [0] * (len_scc)

    new_graph = [set() for _ in range(len_scc)]
    for i in range(len_scc):
        for v in scc[i]:
            for x in graph[v]:
                if i != idx_in_scc[x]:
                    degree[idx_in_scc[x]] += 1

    cnt = 0
    for i in range(len_scc):
        if degree[i] == 0:
            cnt += 1

    if cnt == 0:
        cnt = 1

    ans.append(cnt)

print(*ans, sep='\n')
