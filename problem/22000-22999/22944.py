from collections import deque
import sys
input = sys.stdin.readline

n, h, d = map(int, input().split())

li = [list(input().rstrip()) for _ in range(n)]

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)
dq = deque()

visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if li[i][j] == 'S':
            dq.append((i, j, h, 0))
            visited[i][j] = h
            break

cnt = 0
while dq:
    cnt += 1
    for _ in range(len(dq)):
        x, y, h, u = dq.popleft()

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]

            if a < 0 or a > n - 1:
                continue
            if b < 0 or b > n - 1:
                continue

            if visited[a][b] >= h + u:
                continue
            visited[a][b] = h + u

            if li[a][b] == 'E':
                print(cnt)
                exit(0)

            umb = u
            if li[a][b] == 'U':
                umb = d

            if umb > 0:
                dq.append((a, b, h, umb - 1))
            elif h > 1:
                dq.append((a, b, h - 1, umb))

print(-1)
