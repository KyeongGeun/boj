import sys
input = sys.stdin.readline

def dfs(n):
    visited = [False] * v
    stack = [(n, 0)]
    farthest = (0, 0)
    visited[n] = True
    while stack:
        x, d = stack.pop()
        for y, w in graph[x]:
            if not visited[y]:
                visited[y] = True
                stack.append((y, d + w))
                if farthest[1] < d + w:
                    farthest = (y, d + w)
    return farthest

v = int(input())

graph = [[] for _ in range(v)]

for _ in range(v):
    li = list(map(int, input().split()))
    for i in range(1, len(li), 2):
        if li[i] == -1:
            break
        graph[li[0] - 1].append((li[i] - 1, li[i + 1]))

print(dfs(dfs(1)[0])[1])