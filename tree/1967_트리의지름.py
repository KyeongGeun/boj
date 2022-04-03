import sys
input = sys.stdin.readline

def dfs(num):
    stack = [(num, 0)]
    visited = [False] * n
    visited[num] = True
    farthest = (0, 0)
    while stack:
        x, d = stack.pop()
        for y, w in graph[x]:
            if not visited[y]:
                visited[y] = True
                stack.append((y, d + w))
                if farthest[1] < d + w:
                    farthest = (y, d + w)
    return farthest

n = int(input())

graph = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))

print(dfs(dfs(0)[0])[1])