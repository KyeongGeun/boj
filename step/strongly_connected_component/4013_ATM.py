import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6 * 5)

def func(N):
    global cnt
    cnt += 1

    visited[N] = True
    idx[N] = cnt
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
            li.append(x)
            idx_in_scc[x] = id
            finished[x] = True

            if x == N:
                scc.append(li)
                break

    return ret

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

scc_graph = [[] for _ in range(len(scc))]
degree = [0] * (len(scc))
for i in range(1, n + 1):
    for v in graph[i]:
        if idx_in_scc[i] != idx_in_scc[v]:
            scc_graph[idx_in_scc[i]].append(idx_in_scc[v])
            degree[idx_in_scc[v]] += 1

atm = [0]
for _ in range(n):
    atm.append(int(input()))

sum_scc = [0] * len(scc)
for i in range(len(scc)):
    for v in scc[i]:
        sum_scc[i] += atm[v]

s, p = map(int, input().split())
li = list(map(int, input().split()))

check = [False] * len(scc) # 레스토랑: True

for v in li:
    check[idx_in_scc[v]] = True

memo = [-1] * (len(scc)) 
def dfs(N):
    ret = 0
    if memo[N] != -1:
        return memo[N]

    for v in scc_graph[N]:
            ret = max(ret, dfs(v))
    
    if ret != 0 or check[N]:
        ret += sum_scc[N]

    memo[N] = ret
    return ret

print(dfs(idx_in_scc[s]))
