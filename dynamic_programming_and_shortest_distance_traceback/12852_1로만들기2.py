from collections import deque

n = int(input())

def bfs(n):
    dq = deque([[n, 0, [n]]])
    visited = [0] * (n + 1)
    while dq:
        x, d, li = dq.popleft()

        if x == 1:
            return d, li
            
        if x % 3 == 0 and visited[x // 3] == 0:
            dq.append([x // 3, d + 1, li + [x // 3]])
            visited[x // 3] = 1
        if x % 2 == 0 and visited[x // 2] == 0:
            dq.append([x // 2, d + 1, li + [x // 2]])
            visited[x // 2] = 1
        if visited[x - 1] == 0:
            dq.append([x - 1, d + 1, li + [x - 1]])
            visited[x - 1] = 1

d, li = bfs(n)
print(d)
print(*li)