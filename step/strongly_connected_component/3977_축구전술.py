import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def func(N):
    global cnt
    cnt += 1

    visited[N] = True
    idx[N] = cnt
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

    graph = [[] for _ in range(n)]

    cnt = 0
    idx = [0] * (n + 1)
    visited = [False] * (n)
    finished = [False] * (n)
    stack = []
    scc = []
    idx_in_scc = [0] * (n)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    for i in range(n):
        if not visited[i]:
            func(i)

    l = len(scc)
    degree = [0] * l
    scc_graph = [[] for _ in range(l)]
    for i in range(n):
        for v in graph[i]:
            if idx_in_scc[i] != idx_in_scc[v]:
                degree[idx_in_scc[v]] = 1
    
    cnt = 0
    for i in range(l):
        if degree[i] == 0:
            cnt += 1
    
    if cnt == 0:
        for i in range(n):
            ans.append(i)
    elif cnt == 1:
        for i in range(l):
            if degree[i] == 0:
                for v in sorted(scc[i]):
                    ans.append(v)
    else:
        ans.append('Confused')

    input()
    ans.append('')
else:
    ans.pop()

print(*ans, sep='\n')
