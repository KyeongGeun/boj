import sys
input = sys.stdin.readline

def dfs(v):
    log.add(v)

    li = []
    for value in edge[v]:
        if value not in log:
            li += dfs(value)

    return [v] + li

n = int(input())
edge = [[] for _ in range(n + 1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

log = set()

d = dfs(1)
print(len(d) - 1)