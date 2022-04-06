import sys
input = sys.stdin.readline

def dfs(x, pre):
    visited[x] = True
    for v in graph[x]:
        if v == pre:
            continue
        if visited[v] == True:
            return False
        if not dfs(v, x):
            return False
    return True

case = 1
while True:
    n, m = map(int, input().split())
    
    if n == 0:
        break

    graph = [[] for _ in range(n)]
    visited = [False] * n
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    tree = 0
    for i in range(n):
        if dfs(i, -1):
            tree += 1

    if tree > 1:
        print(f'Case {case}: A forest of {tree} trees.')
    elif tree == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: No trees.')
    case += 1