from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def find(x):
    if parent[x[0]][x[1]][0] < 0:
        return [x[0], x[1]]

    parent[x[0]][x[1]] = find(parent[x[0]][x[1]])
    return parent[x[0]][x[1]]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False

    if x[0] + x[1] < y[0] + y[1]:
        x, y = y, x

    parent[y[0]][y[1]][0] += parent[x[0]][x[1]][0]
    parent[y[0]][y[1]][1] += parent[x[0]][x[1]][1]
    parent[x[0]][x[1]] = [y[0], y[1]]

    return True


n, m = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(n)]

parent = [[[-1, -1] for _ in range(m)] for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

for i in range(n):
    for j in range(m):
        if li[i][j] == 1 and not visited[i][j]:
            cnt += 1
            dq = deque([[i, j]])
            visited[i][j] == True

            while dq:
                x, y = dq.popleft()

                for k in range(4):
                    a = x + dx[k]
                    b = y + dy[k]

                    if 0 <= a < n and 0 <= b < m and li[a][b] == 1 and not visited[a][b]:
                        union([i, j], [a, b])
                        dq.append([a, b])
                        visited[a][b] = True

edge = []

for i in range(n):
    for j in range(m):
        if li[i][j] == 1:
            for k in range(4):
                w = -1
                a = i
                b = j

                while True:
                    w += 1
                    a += dx[k]
                    b += dy[k]

                    if 0 <= a < n and 0 <= b < m:
                        if li[a][b] == 0:
                            continue
                        elif w <= 1:
                            break
                        else:
                            if find([i, j]) != find([a, b]):
                                edge.append((w, [i, j], [a, b]))
                            break
                    else:
                        break

edge.sort()

ans = 0
cnt2 = 0
for w, x, y in edge:
    if union(x, y):
        ans += w
        cnt2 += 1
        if cnt2 == cnt - 1:
            break
else:
    ans = -1

print(ans)
