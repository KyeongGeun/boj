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
        if not finished[v]:
            ret = min(ret, idx[v])

    if ret == idx[N]:
        li = []
        id = len(scc)
        while stack:
            x = stack.pop()

            li.append(x)
            scc_idx[x] = id
            finished[x] = True

            if x == N:
                scc.append(li)
                break

    return ret


k, n = map(int, input().split())

graph = [[] for _ in range(2 * k + 1)]

for _ in range(n):
    a, a1, b, b1, c, c1 = input().split()
    a = int(a) if a1 == 'R' else -int(a)
    b = int(b) if b1 == 'R' else -int(b)
    c = int(c) if c1 == 'R' else -int(c)

    graph[-a].append(b)
    graph[-a].append(c)
    graph[-b].append(a)
    graph[-b].append(c)
    graph[-c].append(a)
    graph[-c].append(b)

visited = [False] * (2 * k + 1)
finished = [False] * (2 * k + 1)
idx = [0] * (2 * k + 1)
scc_idx = [0] * (2 * k + 1)
scc = []
stack = []
cnt = 0

for i in range(1, k + 1):
    if not visited[i]:
        func(i)
    if not finished[-i]:
        func(-i)

for i in range(1, k + 1):
    if scc_idx[i] == scc_idx[-i]:
        print(-1)
        exit(0)

pair = [(scc_idx[v], v) for v in range(-k, k + 1) if v != 0]
pair.sort(reverse=True)

bool = ['-'] * (2 * k + 1)
for _, v in pair:
    if bool[v] == '-':
        bool[v] = 'B'
        bool[-v] = 'R'

print(''.join(bool[1:k + 1]))
