from collections import deque
import sys
input = sys.stdin.readline

def bfs():

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]

            if 0 <= a < n and 0 <= b < m:
                if li[a][b] == 0:
                    li[a][b] = li[x][y] + 1
                elif li[a][b] > li[x][y] + 1:
                    li[a][b] = li[x][y] + 1
                else:
                    continue
                q.append((a, b))


m, n = map(int, input().split()) # 2 <= m, n <= 1000

li = [list(map(int, input().split())) for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if li[i][j] == 1:
            q.append((i, j))

bfs()

maxi = 0
for i in range(n):
    for j in range(m):
        if li[i][j] == 0:
            print(-1)
            sys.exit(0)
        maxi = max(maxi, li[i][j])

print(maxi - 1)